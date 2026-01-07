# Shape & Contour Analyzer

**Status:** Active | **Type:** Computer Vision Dashboard

## Overview
This project is a high-performance, interactive Streamlit dashboard designed to detect, classify, and analyze geometric shapes in images. Built with precision and scalability in mind, it leverages OpenCV for robust feature extraction and contour analysis.

## Key Features
- **Geometric Shape Detection:** Identifies Triangles, Squares, Rectangles, Pentagons, and Circles.
- **Quantitative Analysis:** Computes Area, Perimeter, and Centroids for each object.
- **Interactive Tuning:** Real-time adjustment of thresholding and filtering parameters.
- **Visual Feedback:** High-fidelity overlays of contours and labels.

## Architecture
The project follows a modular "Clean Architecture" approach:
- `src/`: Contains pure domain logic (Image processing, Geometry detection).
- `app/`: Contains the presentation layer (Streamlit UI components).
- `tests/`: Unit testing suite.

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   streamlit run app/main.py
   ```
