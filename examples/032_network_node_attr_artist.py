import random

import compas
from compas.artists import Artist
from compas.artists import clear
from compas.datastructures import Network

network = Network.from_obj(compas.get("grid_irregular.obj"))

for node in network.nodes():
    network.node_attribute(node, "weight", random.choice(range(20)))

print(network.summary())

text = {node: str(network.node_attribute(node, "weight")) for node in network.nodes()}

# Visualize network with an artist
clear()
artist = Artist(network)
artist.draw_nodelabels(text)
artist.draw_edges()
