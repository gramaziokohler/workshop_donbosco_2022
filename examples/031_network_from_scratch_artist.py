import random

from compas.artists import Artist
from compas.artists import clear
from compas.datastructures import Network

network = Network()

network.add_edge(1, 2)
network.add_edge(2, 3)
network.add_edge(1, 4)
network.add_edge(4, 5)
network.add_edge(4, 6)

# Add randomly chosen coordinates to each node
for node in network.nodes():
    x = random.choice(range(5))
    y = random.choice(range(5))
    z = random.choice(range(5))
    network.node_attributes(node, "xyz", [x, y, z])

print(network.summary())

clear()
artist = Artist(network)
artist.draw_nodelabels("key")
artist.draw_edges()
