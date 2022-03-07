import compas
from compas.datastructures import Mesh
from compas.artists import Artist
from compas.artists import clear

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))
mesh.flip_cycles()

clear()
artist = Artist(mesh)
artist.draw()
artist.draw_vertexnormals()
