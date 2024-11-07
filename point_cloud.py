import matplotlib.pyplot as plt
import numpy as np
import open3d as o3d

num_points = 5
pcd = np.random.rand(num_points, 3)
# print(pcd)

# Create figure
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter3D(pcd[:, 0], pcd[:, 1], pcd[:, 2])

# label the axes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Random Point Cloud")
# display:
plt.show()
