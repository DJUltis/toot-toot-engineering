#!/usr/bin/env python3
import math
import re
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

DB_PATH = Path("MyMentalPalaceDB.md")

REFRESH_MS = 1500
ANIMATION_MS = 16


class NavigatorApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("TTDB Navigator")
        self.geometry("1200x800")
        self.minsize(900, 600)

        self._file_mtimes = {}
        self._auto_refresh = tk.BooleanVar(value=True)
        self._db_records: dict[str, dict] = {}
        self._db_order: list[str] = []
        self._db_selected_id: str | None = None
        self._db_coords: dict[str, tuple[float, float]] = {}

        self._globe_rot_lat = 0.0
        self._globe_rot_lon = 0.0
        self._globe_target_lat = 0.0
        self._globe_target_lon = 0.0
        self._globe_animating = False
        self._globe_items: dict[int, str] = {}

        self._init_fonts()
        self._build_ui()
        self._refresh_all(force=True)
        self.after(REFRESH_MS, self._poll_files)

    def _init_fonts(self) -> None:
        base = tkfont.nametofont("TkDefaultFont")
        self.font_body = base.copy()
        self.font_body.configure(size=11)

        self.font_h1 = base.copy()
        self.font_h1.configure(size=18, weight="bold")
        self.font_h2 = base.copy()
        self.font_h2.configure(size=16, weight="bold")
        self.font_h3 = base.copy()
        self.font_h3.configure(size=14, weight="bold")
        self.font_h4 = base.copy()
        self.font_h4.configure(size=13, weight="bold")

        self.font_code = tkfont.Font(
            family="Courier New",
            size=10,
        )

    def _build_ui(self) -> None:
        top = ttk.Frame(self, padding=10)
        top.pack(fill="x")

        self.current_selection_var = tk.StringVar(value="Selected: (loading)")
        current_selection = ttk.Label(
            top,
            textvariable=self.current_selection_var,
            font=("TkDefaultFont", 12, "bold"),
        )
        current_selection.pack(side="left")

        refresh_btn = ttk.Button(top, text="Refresh", command=self._refresh_all)
        refresh_btn.pack(side="right")

        auto_refresh = ttk.Checkbutton(
            top,
            text="Auto refresh",
            variable=self._auto_refresh,
            onvalue=True,
            offvalue=False,
        )
        auto_refresh.pack(side="right", padx=(0, 12))

        pane = ttk.Panedwindow(self, orient="horizontal")
        pane.pack(fill="both", expand=True)

        left = ttk.Frame(pane, padding=(8, 8, 4, 8))
        right = ttk.Frame(pane, padding=(4, 8, 8, 8))
        pane.add(left, weight=1)
        pane.add(right, weight=3)

        list_label = ttk.Label(left, text="Records")
        list_label.pack(anchor="w")

        self.db_listbox = tk.Listbox(
            left,
            font=self.font_body,
            background="#111318",
            foreground="#e9e9f0",
            selectbackground="#364156",
            selectforeground="#ffffff",
            relief="flat",
            activestyle="none",
        )
        self.db_listbox.pack(side="left", fill="both", expand=True)
        list_scroll = ttk.Scrollbar(left, orient="vertical", command=self.db_listbox.yview)
        list_scroll.pack(side="right", fill="y")
        self.db_listbox.configure(yscrollcommand=list_scroll.set)
        self.db_listbox.bind("<<ListboxSelect>>", self._on_db_list_select)

        right_pane = ttk.Panedwindow(right, orient="vertical")
        right_pane.pack(fill="both", expand=True)

        text_frame = ttk.Frame(right_pane)
        globe_frame = ttk.Frame(right_pane)
        right_pane.add(text_frame, weight=3)
        right_pane.add(globe_frame, weight=2)

        self.db_view = tk.Text(
            text_frame,
            wrap="word",
            font=self.font_body,
            padx=12,
            pady=12,
            background="#0f0f12",
            foreground="#e9e9f0",
            insertbackground="#e9e9f0",
            relief="flat",
        )
        self.db_view.pack(side="left", fill="both", expand=True)
        text_scroll = ttk.Scrollbar(text_frame, orient="vertical", command=self.db_view.yview)
        text_scroll.pack(side="right", fill="y")
        self.db_view.configure(yscrollcommand=text_scroll.set)
        self._apply_text_tags(self.db_view)
        self.db_view.configure(state="disabled")

        self.globe = tk.Canvas(
            globe_frame,
            background="#08090c",
            highlightthickness=0,
        )
        self.globe.pack(fill="both", expand=True)
        self.globe.bind("<Configure>", self._on_globe_resize)
        self.globe.bind("<Button-1>", self._on_globe_click)

    def _apply_text_tags(self, text: tk.Text) -> None:
        text.tag_configure("h1", font=self.font_h1, foreground="#ffd166")
        text.tag_configure("h2", font=self.font_h2, foreground="#f4a261")
        text.tag_configure("h3", font=self.font_h3, foreground="#e76f51")
        text.tag_configure("h4", font=self.font_h4, foreground="#e9c46a")
        text.tag_configure("bullet", lmargin1=18, lmargin2=36)
        text.tag_configure("quote", foreground="#a7a7b3", lmargin1=18, lmargin2=36)
        text.tag_configure("code", font=self.font_code, foreground="#c4f1ff")
        text.tag_configure("fence", font=self.font_code, foreground="#6c7a89")
        text.tag_configure("rule", foreground="#39424e")
        text.tag_configure("muted", foreground="#a7a7b3")
        text.tag_configure("link", foreground="#7cc7ff", underline=True)

    def _poll_files(self) -> None:
        if self._auto_refresh.get():
            self._refresh_all()
        self.after(REFRESH_MS, self._poll_files)

    def _refresh_all(self, force: bool = False) -> None:
        db_text = self._read_if_changed(DB_PATH, force=force)
        if db_text is not None:
            self._update_db_data(db_text)

    def _read_if_changed(self, path: Path, force: bool = False) -> str | None:
        try:
            stat = path.stat()
        except FileNotFoundError:
            return f"File not found: {path}"

        last = self._file_mtimes.get(path)
        if not force and last == stat.st_mtime:
            return None

        self._file_mtimes[path] = stat.st_mtime
        return path.read_text(encoding="utf-8")

    def _render_markdown(self, widget: tk.Text, content: str) -> None:
        widget.configure(state="normal")
        widget.delete("1.0", "end")
        self._insert_markdown(widget, content)
        widget.configure(state="disabled")

    def _insert_markdown(self, widget: tk.Text, content: str) -> None:
        in_code = False
        for raw_line in content.splitlines():
            line = raw_line.rstrip("\n")

            if line.startswith("```"):
                in_code = not in_code
                widget.insert("end", line + "\n", ("fence",))
                continue

            if in_code:
                widget.insert("end", line + "\n", ("code",))
                continue

            heading_match = re.match(r"^(#{1,6})\s+(.*)$", line)
            if heading_match:
                level = len(heading_match.group(1))
                tag = f"h{min(level, 4)}"
                widget.insert("end", heading_match.group(2) + "\n", (tag,))
                continue

            if re.match(r"^\s*(-|\*|\d+\.)\s+", line):
                widget.insert("end", line + "\n", ("bullet",))
                continue

            if re.match(r"^\s*>\s+", line):
                widget.insert("end", line + "\n", ("quote",))
                continue

            if re.match(r"^\s*---+\s*$", line):
                widget.insert("end", line + "\n", ("rule",))
                continue

            widget.insert("end", line + "\n")

    def _update_db_data(self, content: str) -> None:
        if content.startswith("File not found:"):
            self._db_records = {}
            self._db_order = []
            self._db_selected_id = None
            self._db_coords = {}
            self._populate_db_list()
            self._render_markdown(self.db_view, content)
            self._render_globe()
            self._update_header()
            return

        records, order, selected, coords = self._parse_db_records(content)
        self._db_records = records
        self._db_order = order
        self._db_coords = coords

        if self._db_selected_id not in self._db_records:
            self._db_selected_id = selected or (order[0] if order else None)

        self._populate_db_list()
        self._render_db_record(self._db_selected_id)
        self._update_header()
        self._center_on_selected()
        self._render_globe()

    def _parse_db_records(
        self, content: str
    ) -> tuple[dict, list[str], str | None, dict[str, tuple[float, float]]]:
        selected = None
        cursor_match = re.search(r"```cursor(.*?)```", content, re.S)
        if cursor_match:
            in_selected = False
            for line in cursor_match.group(1).splitlines():
                stripped = line.strip()
                if stripped.startswith("selected:"):
                    in_selected = True
                    continue
                if in_selected:
                    item_match = re.match(r"-\s*(\S+)", stripped)
                    if item_match:
                        selected = item_match.group(1)
                        break
                    if stripped and not stripped.startswith("-"):
                        break

        records: dict[str, dict] = {}
        order: list[str] = []
        coords: dict[str, tuple[float, float]] = {}
        for block in re.split(r"^\s*---+\s*$", content, flags=re.M):
            lines = [line.rstrip("\n") for line in block.splitlines()]
            header_index = None
            for idx, line in enumerate(lines):
                if line.startswith("@"):
                    header_index = idx
                    break
            if header_index is None:
                continue
            header_line = lines[header_index].strip()
            record_id = header_line.split()[0]
            body = "\n".join(lines[header_index + 1 :]).strip("\n")
            title = None
            for line in body.splitlines():
                title_match = re.match(r"^##\s+(.*)$", line)
                if title_match:
                    title = title_match.group(1).strip()
                    break

            edges = []
            relates_match = re.search(r"relates:([^|]+)", header_line)
            if relates_match:
                for token in relates_match.group(1).split(","):
                    token = token.strip()
                    if not token:
                        continue
                    if ">" in token:
                        edge_type, target = token.split(">", 1)
                    else:
                        edge_type, target = "relates", token
                    edges.append(
                        {
                            "type": edge_type.strip(),
                            "target": target.strip(),
                        }
                    )

            record_coords = self._parse_coords(record_id)
            if record_coords:
                coords[record_id] = record_coords

            records[record_id] = {
                "header": header_line,
                "body": body,
                "title": title,
                "edges": edges,
            }
            order.append(record_id)

        return records, order, selected, coords

    def _parse_coords(self, record_id: str) -> tuple[float, float] | None:
        match = re.match(r"@LAT(-?\d+(?:\.\d+)?)LON(-?\d+(?:\.\d+)?)", record_id)
        if not match:
            return None
        lat = float(match.group(1))
        lon = float(match.group(2))
        return lat, lon

    def _populate_db_list(self) -> None:
        self.db_listbox.delete(0, "end")
        for record_id in self._db_order:
            title = self._db_records.get(record_id, {}).get("title")
            label = f"{record_id} - {title}" if title else record_id
            self.db_listbox.insert("end", label)

        if self._db_selected_id in self._db_order:
            idx = self._db_order.index(self._db_selected_id)
            self.db_listbox.selection_set(idx)
            self.db_listbox.activate(idx)
            self.db_listbox.see(idx)

    def _on_db_list_select(self, event: tk.Event) -> None:
        selection = self.db_listbox.curselection()
        if not selection:
            return
        record_id = self._db_order[selection[0]]
        self._select_db_record(record_id, from_list=True)

    def _select_db_record(self, record_id: str | None, from_list: bool = False) -> None:
        if not record_id or record_id not in self._db_records:
            self._render_markdown(self.db_view, "No records available.")
            return
        self._db_selected_id = record_id
        if not from_list and record_id in self._db_order:
            idx = self._db_order.index(record_id)
            self.db_listbox.selection_clear(0, "end")
            self.db_listbox.selection_set(idx)
            self.db_listbox.activate(idx)
            self.db_listbox.see(idx)
        self._render_db_record(record_id)
        self._update_header()
        self._center_on_selected()
        self._render_globe()

    def _render_db_record(self, record_id: str | None) -> None:
        if not record_id or record_id not in self._db_records:
            self._render_markdown(self.db_view, "No record selected.")
            return
        record = self._db_records[record_id]
        widget = self.db_view
        widget.configure(state="normal")
        widget.delete("1.0", "end")

        widget.insert("end", f"{record_id}\n", ("h2",))
        widget.insert("end", record["header"] + "\n", ("muted",))

        edges = record.get("edges", [])
        if edges:
            widget.insert("end", "\nRelated records\n", ("h3",))
            for idx, edge in enumerate(edges):
                edge_type = edge.get("type") or "relates"
                target = edge.get("target") or ""
                tag = f"link_{record_id}_{idx}"
                widget.tag_configure(tag, foreground="#7cc7ff", underline=True)
                widget.tag_bind(
                    tag,
                    "<Button-1>",
                    lambda _event, rid=target: self._select_db_record(rid),
                )
                widget.tag_bind(
                    tag,
                    "<Enter>",
                    lambda _event: widget.configure(cursor="hand2"),
                )
                widget.tag_bind(
                    tag,
                    "<Leave>",
                    lambda _event: widget.configure(cursor=""),
                )
                widget.insert("end", f"- {edge_type} -> ", ("bullet",))
                if target in self._db_records:
                    widget.insert("end", target + "\n", ("bullet", tag))
                else:
                    widget.insert("end", target + "\n", ("bullet", "muted"))

        body = record.get("body", "")
        if body:
            widget.insert("end", "\n")
            self._insert_markdown(widget, body)

        widget.configure(state="disabled")

    def _update_header(self) -> None:
        if self._db_selected_id:
            self.current_selection_var.set(f"Selected: {self._db_selected_id}")
        else:
            self.current_selection_var.set("Selected: (none)")

    def _center_on_selected(self) -> None:
        record_id = self._db_selected_id
        if not record_id:
            return
        coords = self._db_coords.get(record_id)
        if not coords:
            return
        lat, lon = coords
        # Rotate so the selected point is centered on the front of the globe.
        lat_r = math.radians(lat)
        lon_r = math.radians(lon)
        x = math.cos(lat_r) * math.sin(lon_r)
        y = math.sin(lat_r)
        z = math.cos(lat_r) * math.cos(lon_r)
        rot_lon = -math.atan2(x, z)
        z1 = math.hypot(x, z)
        rot_lat = math.atan2(y, z1)
        self._globe_target_lat = rot_lat
        self._globe_target_lon = rot_lon
        if not self._globe_animating:
            self._globe_animating = True
            self.after(ANIMATION_MS, self._animate_globe)

    def _animate_globe(self) -> None:
        if not self._globe_animating:
            return

        delta_lat = self._angle_delta(self._globe_target_lat, self._globe_rot_lat)
        delta_lon = self._angle_delta(self._globe_target_lon, self._globe_rot_lon)

        if abs(delta_lat) < 0.002 and abs(delta_lon) < 0.002:
            self._globe_rot_lat = self._globe_target_lat
            self._globe_rot_lon = self._globe_target_lon
            self._globe_animating = False
            self._render_globe()
            return

        self._globe_rot_lat += delta_lat * 0.15
        self._globe_rot_lon += delta_lon * 0.15
        self._render_globe()
        self.after(ANIMATION_MS, self._animate_globe)

    def _angle_delta(self, target: float, current: float) -> float:
        delta = target - current
        while delta > math.pi:
            delta -= 2 * math.pi
        while delta < -math.pi:
            delta += 2 * math.pi
        return delta

    def _on_globe_resize(self, event: tk.Event) -> None:
        self._render_globe()

    def _on_globe_click(self, event: tk.Event) -> None:
        item = self.globe.find_withtag("current")
        if not item:
            return
        record_id = self._globe_items.get(item[0])
        if record_id:
            self._select_db_record(record_id)

    def _project_point(self, lat: float, lon: float) -> tuple[float, float, float]:
        lat_r = math.radians(lat)
        lon_r = math.radians(lon)

        x = math.cos(lat_r) * math.sin(lon_r)
        y = math.sin(lat_r)
        z = math.cos(lat_r) * math.cos(lon_r)

        rot_y = self._globe_rot_lon
        cos_y = math.cos(rot_y)
        sin_y = math.sin(rot_y)
        x1 = x * cos_y + z * sin_y
        z1 = -x * sin_y + z * cos_y

        rot_x = self._globe_rot_lat
        cos_x = math.cos(rot_x)
        sin_x = math.sin(rot_x)
        y1 = y * cos_x - z1 * sin_x
        z2 = y * sin_x + z1 * cos_x

        return x1, y1, z2

    def _render_globe(self) -> None:
        globe = self.globe
        globe.delete("all")
        self._globe_items = {}

        width = max(globe.winfo_width(), 200)
        height = max(globe.winfo_height(), 200)
        padding = 6
        radius = width / 2 - padding
        if radius <= 10:
            return

        cx = width / 2
        cy = height / 2

        globe.create_oval(
            cx - radius,
            cy - radius,
            cx + radius,
            cy + radius,
            fill="#0e1117",
            outline="#2a2f3a",
            width=2,
        )
        globe.create_oval(
            cx - radius * 0.92,
            cy - radius * 0.92,
            cx + radius * 0.92,
            cy + radius * 0.92,
            outline="#141824",
            width=1,
        )

        self._draw_graticule(cx, cy, radius)

        if not self._db_coords:
            return

        selected = self._db_selected_id
        nodes_front = []
        nodes_back = []
        selected_point = None
        projections: dict[str, tuple[float, float, float]] = {}
        for record_id, (lat, lon) in self._db_coords.items():
            x, y, z = self._project_point(lat, lon)
            projections[record_id] = (x, y, z)
            if record_id == selected:
                selected_point = (record_id, x, y, z)
            elif z > 0:
                nodes_front.append((record_id, x, y, z))
            else:
                nodes_back.append((record_id, x, y, z))

        for record_id, x, y, z in nodes_back:
            px = cx + x * radius
            py = cy - y * radius
            size = 3
            globe.create_oval(
                px - size,
                py - size,
                px + size,
                py + size,
                fill="#2b303b",
                outline="",
            )

        # Draw typed edges for visible nodes.
        for source_id, record in self._db_records.items():
            edges = record.get("edges", [])
            if not edges:
                continue
            source_proj = projections.get(source_id)
            if not source_proj:
                continue
            sx, sy, sz = source_proj
            if sz <= 0:
                continue
            sxp = cx + sx * radius
            syp = cy - sy * radius
            for edge in edges:
                target_id = edge.get("target")
                if not target_id:
                    continue
                target_proj = projections.get(target_id)
                if not target_proj:
                    continue
                tx, ty, tz = target_proj
                if tz <= 0:
                    continue
                txp = cx + tx * radius
                typ = cy - ty * radius
                is_selected_edge = source_id == selected or target_id == selected
                color = "#2a3a4d" if not is_selected_edge else "#7cc7ff"
                width = 1 if not is_selected_edge else 2
                globe.create_line(sxp, syp, txp, typ, fill=color, width=width)

        for record_id, x, y, z in nodes_front:
            px = cx + x * radius
            py = cy - y * radius
            size = 5
            fill = "#7cc7ff"
            outline = "#0b0b10"
            item = globe.create_oval(
                px - size,
                py - size,
                px + size,
                py + size,
                fill=fill,
                outline=outline,
                width=2,
                tags=("node",),
            )
            self._globe_items[item] = record_id

        if selected_point:
            record_id, x, y, z = selected_point
            px = cx + x * radius
            py = cy - y * radius
            size = 7
            item = globe.create_oval(
                px - size,
                py - size,
                px + size,
                py + size,
                fill="#ffd166",
                outline="#f4a261",
                width=2,
                tags=("node",),
            )
            self._globe_items[item] = record_id
            globe.create_text(
                px,
                py - 14,
                text=record_id,
                fill="#e9e9f0",
                font=("TkDefaultFont", 9, "bold"),
            )

    def _draw_graticule(self, cx: float, cy: float, radius: float) -> None:
        for lon in range(-150, 180, 30):
            points = []
            for lat in range(-90, 91, 6):
                x, y, z = self._project_point(lat, lon)
                visible = z > 0
                if visible:
                    px = cx + x * radius
                    py = cy - y * radius
                    points.append((px, py, visible))
                else:
                    points.append((0, 0, visible))
            self._draw_visible_line(points)

        for lat in range(-60, 90, 30):
            points = []
            for lon in range(-180, 181, 6):
                x, y, z = self._project_point(lat, lon)
                visible = z > 0
                if visible:
                    px = cx + x * radius
                    py = cy - y * radius
                    points.append((px, py, visible))
                else:
                    points.append((0, 0, visible))
            self._draw_visible_line(points)

    def _draw_visible_line(self, points: list[tuple[float, float, bool]]) -> None:
        line = []
        for px, py, visible in points:
            if visible:
                line.append((px, py))
            elif line:
                if len(line) >= 2:
                    self.globe.create_line(
                        *self._flatten(line),
                        fill="#1a1f2a",
                        width=1,
                    )
                line = []
        if len(line) >= 2:
            self.globe.create_line(
                *self._flatten(line),
                fill="#1a1f2a",
                width=1,
            )

    def _flatten(self, points: list[tuple[float, float]]) -> list[float]:
        flat: list[float] = []
        for x, y in points:
            flat.extend([x, y])
        return flat


def main() -> None:
    app = NavigatorApp()
    app.mainloop()


if __name__ == "__main__":
    main()
