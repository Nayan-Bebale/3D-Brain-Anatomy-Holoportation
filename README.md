# 3D Brain Tumor Visualization with Holoportation

This project visualizes brain images with and without tumors by transforming 2D medical images into 3D representations. Using volume rendering and image depth mapping, we aim to provide a more immersive view of brain anatomy to support medical professionals in diagnosing and studying brain tumors.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Demonstration](#demonstration)
6. [File Descriptions](#file-descriptions)
7. [Future Improvements](#future-improvements)

---

## Project Overview

In medical imaging, understanding the depth and positioning of structures within the brain can aid in diagnosing issues such as tumors. This project uses **holoportation** techniques to create 3D visualizations of 2D brain scans, which may improve the clarity and insights available to medical professionals.

The main objectives of the project:
- **3D Surface Plotting**: Generate a 3D plot from 2D brain images, showcasing the spatial positioning of brain features.
- **Volume Rendering**: Perform volume rendering to highlight different tissue densities and tumor regions based on threshold settings.

---

## Dataset

The dataset, located in the `brain_tumor_dataset` folder, includes brain images categorized as either containing a tumor (`yes` folder) or not (`no` folder). Each image in this dataset allows for:
- Comparison of brain images with and without tumors.
- Visualization of differences in brain structure due to tumor presence.

### Example Dataset Structure:
```plaintext
brain_tumor_dataset/
├── yes/       # Images with brain tumors
│   ├── Y1.jpg
│   ├── Y2.jpg
│   └── ...
└── no/        # Images without brain tumors
    ├── N1.jpg
    ├── N2.jpg
    └── ...
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/3D-Brain-Anatomy-Holoportation.git
   cd 3D-Brain-Anatomy-Holoportation
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. 3D Surface Plot
To create a 3D surface plot of a 2D image:
```bash
python image_3d_surface_plot.py
```
This script reads a 2D image and renders it as a 3D surface with adjustable transparency and color mapping.

### 2. Volume Rendering
To generate a volume-rendered 3D representation:
```bash
python volume_render.py
```
This script applies volume rendering techniques to highlight denser areas, potentially helping to visualize tumor regions.

---

## Demonstration

Here's the "Comparison of Brain Images With and Without Tumors" section with the images displayed side-by-side for better visual comparison.

---

### Comparison of Brain Images With and Without Tumors

Below, we compare two images side-by-side to highlight the differences between a brain scan with a tumor and one without. The visualizations showcase how tumors alter brain structure, which becomes clearer with 3D rendering.

| Brain Without Tumor | Brain With Tumor |
|---------------------|------------------|
| <img src="https://raw.githubusercontent.com/Nayan-Bebale/3D-Brain-Anatomy-Holoportation/refs/heads/main/brain_tumor_dataset/no/1%20no.jpeg" alt="Without Tumor" width="310" height="350"> | ![Tumor Present](https://raw.githubusercontent.com/Nayan-Bebale/3D-Brain-Anatomy-Holoportation/refs/heads/main/brain_tumor_dataset/yes/Y10.jpg) |

The 3D transformations provide an interactive way to explore these differences, helping to understand the spatial changes caused by tumor presence.

--- 

This layout will place the two images beside each other for a direct visual comparison in the README.

### Video Demonstrations
We have provided video examples to illustrate the transformation process from 2D images to 3D holographic visualizations.
- **Demonstrations**: [Tumor Visualization Video](./videos/tumor_video.mp4)

---

## File Descriptions

- **image_3d_surface_plot.py**: Generates a 3D surface plot from a 2D image. Useful for creating an interactive view of the brain image in 3D.
- **volume_render.py**: Implements volume rendering techniques to simulate depth and highlight areas with different opacity thresholds.
- **brain_tumor_dataset**: Contains the dataset, divided into folders `yes` (with tumors) and `no` (without tumors).

---

## Future Improvements

Future enhancements could include:
- **Automated Detection**: Implementing machine learning algorithms to detect tumors automatically.
- **Interactive Controls**: Adding interactive controls to adjust thresholding and opacity on the 3D plots.
- **Dataset Expansion**: Incorporating more detailed brain datasets for higher accuracy in 3D rendering and tumor mapping.
