import open3d as o3d
import matplotlib.pyplot as plt
import numpy as np

bunny = o3d.data.BunnyMesh()
mesh = o3d.io.read_triangle_mesh("Y2.ply")

# visualize
# mesh.compute_vertex_normals()
# o3d.visualization.draw_geometries([mesh])

# sample 1000 points:
pcd = mesh.sample_points_uniformly(number_of_points=1000, use_triangle_normal=False)

# visualize
o3d.visualization.draw_geometries([pcd])