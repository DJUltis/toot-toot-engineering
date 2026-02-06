# Toot-Toot Engineering Prompt

## Build a Complete TTN With Per-Node TTDB Sync (6 Devices)

## Deliverables
- specs
- functional software/firmware for all devices
- deployment steps for putting the software/firmware on the respective devices
- a complete guide for humans to configure all devices and perform Acceptance Tests

Each device runs a **local TTDB (MyMentalPalaceDB variant)** and participates in discovery, semantic storage, and gossip-style synchronization so that all nodes progressively know about each other.
Refer to the documents in the "standards" folder and "RFCs" folder for specifications and guidance of the Toot Toot Network and Toot Toot Database (TTDB).
---

## Devices (exactly six)

1. Windows Machine – TTN Hub, visualization, development, optional MQTT broker
2. UNIHIKER K10 – Mesh console UI, serial gateway, semantic edge node
3. Heltec WiFi LoRa 32 V4 #1 – Meshtastic radio node
4. Heltec WiFi LoRa 32 V4 #2 – Meshtastic radio node
5. Heltec WiFi LoRa 32 V4 #3 – Meshtastic radio node
6. LILYGO T-Deck – Meshtastic radio node with keyboard UI

---

## Prime Directive

Every device:
- Maintains a **local TTDB**
- Stores knowledge about itself and peers
- Records message history and derived semantic links
- Exchanges TTDB diffs with peers until the network converges

No single authoritative database exists.

---

## A. Network Architecture

### A1. Roles

- Meshtastic radio layer: Heltec nodes + T-Deck
- UI and gateway: K10 (USB serial to one Meshtastic node)
- Hub: Windows machine (aggregation, visualization, optional MQTT)

### A2. Interfaces

- LoRa: Meshtastic mesh
- USB serial: K10 ↔ Heltec #1
- Wi-Fi: optional high-speed TTDB diff sync

### A3. Identity Model

Each node has a stable `ttn_node_id`:
- If GPS available: `gps:<lat>,<lon>` (rounded to 6 decimals)
- Else: `hw:<chip_family>:<mac>`

Store Meshtastic `node_num` as an attribute when applicable.

---

## B. TTDB / MyMentalPalaceDB Schema

TTDB is **append-only JSON lines**, with periodic compaction.

### B1. Record Kinds

#### node
```json
{
  "kind": "node",
  "id": "hw:esp32s3:aa:bb:cc",
  "label": "K10",
  "roles": ["ui_console", "serial_gateway"],
  "interfaces": {"usb": true, "wifi": true, "lora": false},
  "capabilities": {"display": true, "keyboard": false}
}
```

#### presence
```json
{
  "kind": "presence",
  "observer_id": "hw:k10",
  "subject_id": "hw:heltec1",
  "time_utc": "2026-02-06T14:22:00Z",
  "via": "meshtastic",
  "signal": {"rssi": -87, "snr": 7.5}
}
```

#### meshtastic_packet
```json
{
  "kind": "meshtastic_packet",
  "time_utc": "2026-02-06T14:22:01Z",
  "rx_by_id": "hw:k10",
  "from_node_num": 123456,
  "portnum": "TEXT_MESSAGE_APP",
  "payload_b64": "SGVsbG8gTWVzaCE="
}
```

#### message
```json
{
  "kind": "message",
  "id": "msg-abc123",
  "time_utc": "2026-02-06T14:22:01Z",
  "from_id": "hw:heltec1",
  "channel": "field",
  "content": "Hello Mesh",
  "content_type": "text"
}
```

#### edge
```json
{
  "kind": "edge",
  "from": "hw:k10",
  "to": "hw:heltec1",
  "type": "observed",
  "time_utc": "2026-02-06T14:22:01Z",
  "weight": 0.8
}
```

#### sync_diff
```json
{
  "kind": "sync_diff",
  "from_id": "hw:k10",
  "to_id": "hw:windows",
  "time_utc": "2026-02-06T14:23:00Z",
  "summary": {"new_records": 12, "bytes": 4096}
}
```

---

## C. Meshtastic → TTDB Mapping Rules

1. NodeInfo → node record update + capability edges
2. Position → message (position) + located_at edge + presence
3. Telemetry → message (telemetry) + observed edge
4. Text → message (text) + mention edges
5. Any packet → presence of sender

Raw payloads are always preserved.

---

## D. K10 ↔ Meshtastic Serial Protocol Map

### D1. Physical Layer

- USB CDC ACM
- 115200 baud, 8N1

### D2. Logical Modes

#### Line / CLI Mode
- Parse human-readable output
- Used for fallback and diagnostics

#### Protobuf Framed Mode
- Binary framed messages
- Supports send, receive, subscribe, node info

### D3. Gateway Responsibilities

- Ingest serial data → meshtastic_packet
- Normalize → message
- Link → presence + semantic edges
- Store in TTDB

### D4. Supported Commands

- LIST_NODES
- GET_NODEINFO <node>
- SEND_TEXT <dst> <text>
- SUBSCRIBE_ALL
- EXPORT_TTDB_DIFF
- IMPORT_TTDB_DIFF

---

## E. K10 Mesh Console UI (LVGL)

### Screens

1. Inbox – chronological message list
2. Compose – destination select + text input
3. Nodes – known nodes with last-seen
4. Map-lite – simple position list
5. Sync – TTDB diff status and controls
6. Diagnostics – serial + memory stats

### Storage

- ttdb.log (append-only)
- ttdb.snapshot.json (compacted)

---

## F. Gossip Sync

### Transport Options

1. Wi-Fi HTTP endpoints
2. Meshtastic chunked message drip
3. USB serial sneakernet via K10

### Diff Strategy

- Content-addressed records (sha256)
- Exchange recent-hash lists
- Transmit only missing records

---

## G. Acceptance Tests

1. K10 sends message, received by at least two radio nodes
2. Windows hub displays all six nodes
3. Power-cycle one Heltec, rediscovery occurs
4. TTDB compaction does not lose data
5. Node without Wi-Fi learns about Windows via mesh diffs

---

## Design Principles

- Append-only durability
- Semantic edges as first-class citizens
- Transport-agnostic memory
- Observable, inspectable behavior

This defines the canonical **TTN + TTDB reference build** for six heterogeneous devices.

