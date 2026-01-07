# Shape & Contour Analyzer

![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square) [![Live App](https://img.shields.io/badge/Streamlit-Live_Demo-FF4B4B?style=flat-square&logo=streamlit)](https://shape-contour-analyzer.streamlit.app/)

## Overview
This repository contains the **Shape & Contour Analyzer**, an interactive Computer Vision tool developed as a Digital Assignment for the Semester 8 Computer Vision course. The application leverages OpenCV and Streamlit to provide real-time geometric analysis, contour detection, and feature extraction of shapes within images.

## Features
- **Geometric Classification**: Accurately classifies shapes including Triangles, Squares, Rectangles, Pentagons, and Circles.
- **Quantitative Metrics**: Automatically calculates Area, Perimeter, and Centroid coordinates for every detected object.
- **Dynamic Parameter Tuning**: Allows users to fine-tune Canny edge detection thresholds and morphological filters in real-time.
- **Visualization**: Provides high-fidelity visual overlays of contours and centroids directly on the processed image.

## Architecture
The codebase implements a **Modular Layered Architecture** to ensure separation of concerns and maintainability:

- **Core Logic (`src/`)**: Handles all domain-specific computer vision tasks (preprocessing, detection, analysis) independent of the UI.
- **Presentation Layer (`app/`)**: Manages the Streamlit interface, user interactions, and state management.
- **Testing (`tests/`)**: Contains unit tests to validate the accuracy of shape detection algorithms.

## Project Structure
```
├── app/                  # Frontend Application
│   ├── ui/               # Reusable UI components (Sidebar, Dashboard)
│   └── main.py           # Application Entry Point
├── src/                  # Core Computer Vision Libraries
│   ├── analyzer.py       # Pipeline Orchestration
│   ├── detectors.py      # Shape Classification Logic
│   ├── models.py         # Data Classes and Types
│   └── processors.py     # Image Processing Utilities
├── tests/                # Unit Tests
└── requirements.txt      # Project Dependencies
```

## Getting Started

### Prerequisites
- Python 3.8+

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jaideepkathiresan/Shape-and-Contour-Analyzer.git
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
Launch the dashboard locally using Streamlit:
```bash
streamlit run app/main.py
```
