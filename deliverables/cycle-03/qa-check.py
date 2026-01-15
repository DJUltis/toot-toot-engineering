#!/usr/bin/env python3
import math
from pathlib import Path

stl_path = Path('bonsai-marioland.stl')

def parse_triangles(text):
    tris = []
    verts = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith('vertex'):
            _, xs, ys, zs = line.split()
            verts.append((float(xs), float(ys), float(zs)))
            if len(verts) == 3:
                tris.append(verts)
                verts = []
    return tris

text = stl_path.read_text(encoding='ascii', errors='ignore')
tris = parse_triangles(text)

edge_counts = {}

def key(v):
    return (round(v[0], 4), round(v[1], 4), round(v[2], 4))

for tri in tris:
    v1, v2, v3 = tri
    verts = [key(v1), key(v2), key(v3)]
    edges = [(verts[0], verts[1]), (verts[1], verts[2]), (verts[2], verts[0])]
    for a, b in edges:
        if a > b:
            a, b = b, a
        edge_counts[(a, b)] = edge_counts.get((a, b), 0) + 1

boundary_edges = sum(1 for c in edge_counts.values() if c == 1)
nonmanifold_edges = sum(1 for c in edge_counts.values() if c > 2)

print('triangles', len(tris))
print('boundary_edges', boundary_edges)
print('nonmanifold_edges', nonmanifold_edges)
