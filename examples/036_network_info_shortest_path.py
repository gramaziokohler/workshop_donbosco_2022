import random

import compas
from compas.artists import Artist
from compas.artists import clear
from compas.datastructures import Network
from compas.utilities import pairwise

network = Network.from_obj(compas.get("grid_irregular.obj"))

# Select random nodes + shortest path
start = random.choice(list(network.leaves()))
goal = random.choice(list(set(network.leaves()) - set([start])))
nodes = network.shortest_path(start, goal)

nodecolor = {}
edgecolor = {}

for u, v in pairwise(nodes):
    nodecolor[v] = (0, 1, 0)
    edgecolor[u, v] = edgecolor[v, u] = (0, 1, 0)

nodecolor[start] = (1, 0, 0)
nodecolor[goal] = (0, 0, 1)

print(network.summary())

clear()
artist = Artist(network)
artist.draw_nodelabels(color=nodecolor)
artist.draw_edges(color=edgecolor)
