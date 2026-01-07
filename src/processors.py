import cv2
import numpy as np
from typing import Tuple

class ImageProcessor:
    """Handles low-level image processing operations."""

    @staticmethod
    def to_grayscale(image: np.ndarray) -> np.ndarray:
        """Convert BGR image to grayscale."""
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def apply_blur(image: np.ndarray, kernel_size: int = 5) -> np.ndarray:
        """Apply Gaussian blur to reduce noise."""
        # Kernel size must be odd
        k = kernel_size if kernel_size % 2 == 1 else kernel_size + 1
        return cv2.GaussianBlur(image, (k, k), 0)

    @staticmethod
    def detect_edges(image: np.ndarray, threshold1: int, threshold2: int) -> np.ndarray:
        """Apply Canny edge detection."""
        return cv2.Canny(image, threshold1, threshold2)

    @staticmethod
    def get_contours(edged_image: np.ndarray) -> Tuple[np.ndarray, ...]:
        """Find contours in an edged image."""
        contours, _ = cv2.findContours(
            edged_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        return contours
