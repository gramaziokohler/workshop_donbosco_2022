import random

import compas
from compas.artists import Artist
from compas.artists import clear
from compas.datastructures import Mesh
from compas.geometry import Cylinder
from compas.utilities import flatten

mesh = Mesh.from_off(compas.get("tubemesh.off"))

start = random.choice(list(mesh.edges()))
loop = mesh.edge_loop(start)
strip = [mesh.edge_faces(*edge) for edge in mesh.edge_strip(start)]
strip[:] = list(set(flatten(strip)))

edgecolor = {}
for edge in loop:
    edgecolor[edge] = (0, 1, 0)

edgecolor[start] = (1, 0, 0)

facecolor = {}
for face in strip:
    facecolor[face] = (1, 0.8, 0.8)

clear()
artist = Artist(mesh)
artist.draw_faces(color=facecolor)

for edge in edgecolor:
    o = mesh.edge_midpoint(*edge)
    n = mesh.edge_direction(*edge)
    h = mesh.edge_length(*edge)

    cylinder = Cylinder([(o, n), 0.02], h)
    artist = Artist(cylinder, color=(0, 1, 0))
    artist.draw()
