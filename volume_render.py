import numpy as np
import matplotlib.pyplot as plt
import cv2


def volume_render(data, threshold):
    image = np.zeros(data.shape[:2])
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Cast a ray from the pixel towards the back of the volume
            ray = np.array([i, j, 0])
            direction = np.array([0, 0, 1])
            # Accumulate opacity and distance along the ray

            opacity = 0
            distance = 0

            while True:
                # Check if the ray leaves the volume
                if distance >= min(data.shape):
                    break
                # Calculate the index of the current voxel
                voxel_index = np.clip(ray + distance * direction, 0, data.shape[0] - 1).astype(int)

                # Extract the voxel value
                voxel_value = data[voxel_index[0], voxel_index[1]]

                # Check if the voxel value is above the threshold
                if voxel_value > threshold:
                    opacity += voxel_value
                    break
                # Update accumulated opacity and distance
                opacity += 0.1
                distance += 0.1

            # Apply opacity to the pixel
            image[i, j] = opacity

    return image


data = cv2.imread('TCGA_CS_4941_19960909_1.tif', cv2.IMREAD_GRAYSCALE)

render_image = volume_render(data, 0.5)
plt.imshow(render_image, cmap='gray')
plt.show()
