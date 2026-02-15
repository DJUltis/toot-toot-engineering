# Dice TTDB
An inscribed-cube TTDB with equal-distance vertices on the globe. Optional `z` elevation is supported; defaults to `0` at figurative sea level.

```mmpdb
db_id: mmpdb:sample:dice
db_name: "Dice"
coord_increment:
  lat: 1
  lon: 1
collision_policy: southeast_step
timestamp_kind: unix_utc
umwelt:
  umwelt_id: umwelt:tte:agent:dice:v1
  role: dice_librarian
  perspective: "A lattice of dice geometry mapped onto a globe."
  scope: "A single dice-themed TTDB instance."
  constraints:
    - "Coordinates express a figurative geometry, not physical measurement."
  globe:
    frame: "dice_globe"
    origin: "A cube inscribed in a sphere."
    mapping: "Vertices and marks are mapped onto spherical coordinates."
    note: "Optional record header field `z` is supported; default is 0 at sea level."
cursor_policy:
  max_preview_chars: 280
  max_nodes: 25
typed_edges:
  enabled: true
  syntax: "type>@TARGET_ID"
  note: "Typed edges connect matching latitudes and longitudes."
librarian:
  enabled: true
  primitive_queries:
    - "SELECT <record_id>"
    - "FIND <token>"
    - "EDGES <record_id>"
    - "LAST <n>"
    - "STATUS"
  max_reply_chars: 240
  invocation_prefix: "@AI"
```

```cursor
selected:
  - @LAT35.264LON45.0
preview:
  @LAT35.264LON45.0: "Cube vertex at sea level (z=0)."
agent_note: "Dice TTDB. Cube vertices are equal-distance points on the globe."
```

---

@LAT35.264LON45.0 | created:1760000000 | updated:1760000000 | z:0 | relates:lat>@LAT35.264LON135.0,lat>@LAT35.264LON-135.0,lat>@LAT35.264LON-45.0,lon>@LAT-35.264LON45.0

## Cube Vertex NE
North hemisphere vertex at lon 45. Latitudinally linked to other north vertices; longitudinally linked to its south counterpart.

---

@LAT35.264LON135.0 | created:1760000001 | updated:1760000001 | z:0 | relates:lat>@LAT35.264LON45.0,lat>@LAT35.264LON-135.0,lat>@LAT35.264LON-45.0,lon>@LAT-35.264LON135.0

## Cube Vertex NW
North hemisphere vertex at lon 135.

---

@LAT35.264LON-135.0 | created:1760000002 | updated:1760000002 | z:0 | relates:lat>@LAT35.264LON45.0,lat>@LAT35.264LON135.0,lat>@LAT35.264LON-45.0,lon>@LAT-35.264LON-135.0

## Cube Vertex SW
North hemisphere vertex at lon -135.

---

@LAT35.264LON-45.0 | created:1760000003 | updated:1760000003 | z:0 | relates:lat>@LAT35.264LON45.0,lat>@LAT35.264LON135.0,lat>@LAT35.264LON-135.0,lon>@LAT-35.264LON-45.0

## Cube Vertex SE
North hemisphere vertex at lon -45.

---

@LAT-35.264LON45.0 | created:1760000004 | updated:1760000004 | z:0 | relates:lat>@LAT-35.264LON135.0,lat>@LAT-35.264LON-135.0,lat>@LAT-35.264LON-45.0,lon>@LAT35.264LON45.0

## Cube Vertex NE (South)
South hemisphere vertex at lon 45.

---

@LAT-35.264LON135.0 | created:1760000005 | updated:1760000005 | z:0 | relates:lat>@LAT-35.264LON45.0,lat>@LAT-35.264LON-135.0,lat>@LAT-35.264LON-45.0,lon>@LAT35.264LON135.0

## Cube Vertex NW (South)
South hemisphere vertex at lon 135.

---

@LAT-35.264LON-135.0 | created:1760000006 | updated:1760000006 | z:0 | relates:lat>@LAT-35.264LON45.0,lat>@LAT-35.264LON135.0,lat>@LAT-35.264LON-45.0,lon>@LAT35.264LON-135.0

## Cube Vertex SW (South)
South hemisphere vertex at lon -135.

---

@LAT-35.264LON-45.0 | created:1760000007 | updated:1760000007 | z:0 | relates:lat>@LAT-35.264LON45.0,lat>@LAT-35.264LON135.0,lat>@LAT-35.264LON-135.0,lon>@LAT35.264LON-45.0

## Cube Vertex SE (South)
South hemisphere vertex at lon -45.
