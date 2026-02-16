#!/usr/bin/env python3
import json
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


DEFAULT_CONFIG = {
    "storage": {"ttdb_path": "/ttdb_dice_k10.md"},
    "navigation": {
        "wrap_cols": 26,
        "max_body_chars": 260,
        "list_window": 10,
        "detail_lines": 12,
    },
    "theme": {
        "background": "#0f0f12",
        "text": "#e9e9f0",
        "muted": "#6c7a89",
        "accent": "#ffd166",
        "accent2": "#f4a261",
        "select": "#7cc7ff",
    },
}

THEME_PRESETS = {
    "K10 Dark": {
        "background": "#0f0f12",
        "text": "#e9e9f0",
        "muted": "#6c7a89",
        "accent": "#ffd166",
        "accent2": "#f4a261",
        "select": "#7cc7ff",
    },
    "Amber Night": {
        "background": "#0b0a08",
        "text": "#f3e9d6",
        "muted": "#7b6a58",
        "accent": "#f6bd60",
        "accent2": "#e07a5f",
        "select": "#81b29a",
    },
    "Glacier": {
        "background": "#0b1117",
        "text": "#e8f1f7",
        "muted": "#6a8294",
        "accent": "#f4d35e",
        "accent2": "#ee964b",
        "select": "#4ea8de",
    },
}

SAMPLE_TITLES = [
    "Cube Vertex NE",
    "Cube Vertex NW",
    "Cube Vertex SW",
    "Cube Vertex SE",
    "Pip: Face 1 Center",
    "Pip: Face 2 Top-Left",
    "Pip: Face 2 Bottom-Right",
    "Pip: Face 3 Top-Left",
    "Pip: Face 3 Center",
    "Pip: Face 3 Bottom-Right",
]

SAMPLE_DETAIL = [
    "North hemisphere vertex at lon 45.",
    "Lat links to other north vertices.",
    "Lon links to its south counterpart.",
    "Use A/B to step; tilt to scroll.",
]


class ConfiguratorApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("K10 TTDB Configurator")
        self.geometry("980x640")
        self.minsize(900, 600)

        self.config_data = json.loads(json.dumps(DEFAULT_CONFIG))
        self._build_ui()
        self._apply_config_to_vars()
        self._render_preview()

    def _build_ui(self) -> None:
        root = ttk.Frame(self, padding=12)
        root.pack(fill="both", expand=True)

        header = ttk.Label(root, text="K10 TTDB Configurator", font=("TkDefaultFont", 14, "bold"))
        header.pack(anchor="w")

        body = ttk.Panedwindow(root, orient="horizontal")
        body.pack(fill="both", expand=True, pady=(10, 0))

        self.settings_frame = ttk.Frame(body, padding=(0, 0, 12, 0))
        self.preview_frame = ttk.Frame(body)
        body.add(self.settings_frame, weight=1)
        body.add(self.preview_frame, weight=2)

        self._build_settings()
        self._build_preview()
        self._build_footer(root)

    def _build_settings(self) -> None:
        section = ttk.LabelFrame(self.settings_frame, text="Settings", padding=10)
        section.pack(fill="both", expand=True)

        row = 0
        ttk.Label(section, text="TTDB path").grid(row=row, column=0, sticky="w")
        self.ttdb_path_var = tk.StringVar()
        ttk.Entry(section, textvariable=self.ttdb_path_var, width=32).grid(row=row, column=1, sticky="ew")

        row += 1
        ttk.Label(section, text="Wrap columns").grid(row=row, column=0, sticky="w")
        self.wrap_cols_var = tk.IntVar()
        ttk.Spinbox(section, from_=18, to=40, textvariable=self.wrap_cols_var, width=6).grid(
            row=row, column=1, sticky="w"
        )

        row += 1
        ttk.Label(section, text="Max body chars").grid(row=row, column=0, sticky="w")
        self.max_body_var = tk.IntVar()
        ttk.Spinbox(section, from_=120, to=600, increment=10, textvariable=self.max_body_var, width=8).grid(
            row=row, column=1, sticky="w"
        )

        row += 1
        ttk.Label(section, text="List window").grid(row=row, column=0, sticky="w")
        self.list_window_var = tk.IntVar()
        ttk.Spinbox(section, from_=6, to=14, textvariable=self.list_window_var, width=6).grid(
            row=row, column=1, sticky="w"
        )

        row += 1
        ttk.Label(section, text="Detail lines").grid(row=row, column=0, sticky="w")
        self.detail_lines_var = tk.IntVar()
        ttk.Spinbox(section, from_=6, to=16, textvariable=self.detail_lines_var, width=6).grid(
            row=row, column=1, sticky="w"
        )

        preset_frame = ttk.LabelFrame(section, text="Theme presets", padding=8)
        preset_frame.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(12, 6))
        self.preset_var = tk.StringVar(value="K10 Dark")
        ttk.OptionMenu(preset_frame, self.preset_var, "K10 Dark", *THEME_PRESETS.keys(), command=self._apply_preset).pack(
            fill="x"
        )

        theme_frame = ttk.LabelFrame(section, text="Theme colors", padding=8)
        theme_frame.grid(row=6, column=0, columnspan=2, sticky="ew")

        self.color_vars = {}
        for idx, key in enumerate(["background", "text", "muted", "accent", "accent2", "select"]):
            ttk.Label(theme_frame, text=key).grid(row=idx, column=0, sticky="w")
            var = tk.StringVar()
            self.color_vars[key] = var
            ttk.Entry(theme_frame, textvariable=var, width=12).grid(row=idx, column=1, sticky="w")

        button_row = ttk.Frame(section)
        button_row.grid(row=7, column=0, columnspan=2, sticky="ew", pady=(12, 0))
        ttk.Button(button_row, text="Load JSON", command=self._load_config).pack(side="left")
        ttk.Button(button_row, text="Save JSON", command=self._save_config).pack(side="left", padx=(8, 0))

        section.columnconfigure(1, weight=1)

        self._wire_traces()

    def _build_preview(self) -> None:
        header = ttk.Label(self.preview_frame, text="Preview", font=("TkDefaultFont", 12, "bold"))
        header.pack(anchor="w")

        panel = ttk.Frame(self.preview_frame, padding=(0, 8, 0, 0))
        panel.pack(fill="both", expand=True)

        self.list_canvas = tk.Canvas(panel, width=280, height=360, highlightthickness=0)
        self.detail_canvas = tk.Canvas(panel, width=520, height=360, highlightthickness=0)
        self.list_canvas.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
        self.detail_canvas.grid(row=0, column=1, sticky="nsew")

        panel.columnconfigure(0, weight=1)
        panel.columnconfigure(1, weight=2)
        panel.rowconfigure(0, weight=1)

    def _build_footer(self, root: ttk.Frame) -> None:
        self.status_var = tk.StringVar(value="Ready.")
        status = ttk.Label(root, textvariable=self.status_var, foreground="#6c7a89")
        status.pack(anchor="w", pady=(8, 0))

    def _wire_traces(self) -> None:
        for var in [
            self.ttdb_path_var,
            self.wrap_cols_var,
            self.max_body_var,
            self.list_window_var,
            self.detail_lines_var,
        ]:
            var.trace_add("write", lambda *_: self._sync_from_vars())
        for var in self.color_vars.values():
            var.trace_add("write", lambda *_: self._sync_from_vars())

    def _apply_config_to_vars(self) -> None:
        self.ttdb_path_var.set(self.config_data["storage"]["ttdb_path"])
        self.wrap_cols_var.set(self.config_data["navigation"]["wrap_cols"])
        self.max_body_var.set(self.config_data["navigation"]["max_body_chars"])
        self.list_window_var.set(self.config_data["navigation"]["list_window"])
        self.detail_lines_var.set(self.config_data["navigation"]["detail_lines"])
        for key, var in self.color_vars.items():
            var.set(self.config_data["theme"].get(key, ""))

    def _sync_from_vars(self) -> None:
        self.config_data["storage"]["ttdb_path"] = self.ttdb_path_var.get()
        self.config_data["navigation"]["wrap_cols"] = int(self.wrap_cols_var.get())
        self.config_data["navigation"]["max_body_chars"] = int(self.max_body_var.get())
        self.config_data["navigation"]["list_window"] = int(self.list_window_var.get())
        self.config_data["navigation"]["detail_lines"] = int(self.detail_lines_var.get())
        for key, var in self.color_vars.items():
            self.config_data["theme"][key] = var.get().strip()
        self._render_preview()

    def _apply_preset(self, name: str) -> None:
        preset = THEME_PRESETS.get(name)
        if not preset:
            return
        for key, value in preset.items():
            self.color_vars[key].set(value)

    def _render_preview(self) -> None:
        theme = self.config_data["theme"]
        bg = theme["background"]
        text = theme["text"]
        muted = theme["muted"]
        accent = theme["accent"]
        accent2 = theme["accent2"]
        select = theme["select"]

        self.list_canvas.delete("all")
        self.detail_canvas.delete("all")
        self.list_canvas.configure(bg=bg)
        self.detail_canvas.configure(bg=bg)

        self.list_canvas.create_text(14, 18, text="Dice (K10)", anchor="w", fill=accent, font=("TkDefaultFont", 10, "bold"))

        visible = self.config_data["navigation"]["list_window"]
        start = 0
        for idx in range(min(visible, len(SAMPLE_TITLES))):
            title = SAMPLE_TITLES[start + idx]
            y = 40 + idx * 22
            if idx == 0:
                self.list_canvas.create_text(14, y, text=f\"> {title}\", anchor="w", fill=select)
            else:
                self.list_canvas.create_text(14, y, text=f\"  {title}\", anchor="w", fill=text)

        self.detail_canvas.create_text(14, 18, text="Cube Vertex NE", anchor="w", fill=accent2, font=("TkDefaultFont", 11, "bold"))
        self.detail_canvas.create_text(14, 36, text="@LAT35.264LON45.0", anchor="w", fill=muted, font=("TkDefaultFont", 9))

        max_lines = self.config_data["navigation"]["detail_lines"]
        for idx, line in enumerate(SAMPLE_DETAIL[:max_lines]):
            y = 64 + idx * 20
            self.detail_canvas.create_text(14, y, text=line, anchor="w", fill=text)

        self.detail_canvas.create_text(14, 320, text="A/B: prev/next  AB: detail", anchor="w", fill=muted)

    def _load_config(self) -> None:
        path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if not path:
            return
        try:
            data = json.loads(Path(path).read_text(encoding="utf-8"))
        except Exception as exc:
            messagebox.showerror("Load failed", str(exc))
            return
        self.config_data = data
        self._apply_config_to_vars()
        self.status_var.set(f"Loaded {path}")

    def _save_config(self) -> None:
        path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not path:
            return
        try:
            Path(path).write_text(json.dumps(self.config_data, indent=2), encoding="utf-8")
        except Exception as exc:
            messagebox.showerror("Save failed", str(exc))
            return
        self.status_var.set(f"Saved {path}")


def main() -> None:
    app = ConfiguratorApp()
    app.mainloop()


if __name__ == "__main__":
    main()
