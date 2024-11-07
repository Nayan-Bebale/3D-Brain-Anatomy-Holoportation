import numpy as np
import matplotlib.pyplot as plt

# 0 represents no intensity of the color, and 255 represents the maximum intensity.

red = 255
green = 0
blue = 128
# Todo The alpha value represents the transparency or opacity of the color. It ranges from 0 to 255, where 0 means completely transparent and 255 means completely opaque.
alpha = 128
# alpha = 128 indicates a semi-transparent color.

# Normalize RGB values to the range of 0 to 1
norm_red = red / 255.0
norm_green = green / 255.0
norm_blue = blue / 255.0
norm_alpha = alpha / 255.0

# Example RGBA tuple normalized to the range of 0 to 1
rgba = (norm_red, norm_green, norm_blue, norm_alpha)

# Load the 2D image
image_path = "flower.jpg"  # Replace with your image path
img = plt.imread(image_path)

# Create the 3D representation
height, width, _ = img.shape
z_scale = 10  # Scaling factor for the z-axis

# Create a meshgrid for the x, y, and z coordinates
x = np.arange(width)
y = np.arange(height)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X) * z_scale

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the image as a surface
ax.plot_surface(X, Y, Z, facecolors=img/255.0)

# Set labels and aspect ratio
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_box_aspect([1, 1, z_scale])  # Adjust the aspect ratio for proper scaling

plt.show()
