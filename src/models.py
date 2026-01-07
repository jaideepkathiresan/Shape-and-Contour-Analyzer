from dataclasses import dataclass
from typing import Tuple, List, Optional
import numpy as np

@dataclass
class ShapeInfo:
    """Data model representing a detected shape."""
    shape_type: str
    area: float
    perimeter: float
    centroid: Tuple[int, int]
    contour: np.ndarray
    approx_contour: np.ndarray

@dataclass
class ProcessingConfig:
    """Configuration for image processing pipeline."""
    canny_threshold1: int = 50
    canny_threshold2: int = 150
    min_area: float = 100.0
    max_area: float = 50000.0
    gaussian_kernel: int = 5
