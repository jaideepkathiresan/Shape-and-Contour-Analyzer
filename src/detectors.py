import cv2
import numpy as np
from typing import Optional

class ShapeDetector:
    """Logic for identifying geometric shapes from contours."""

    @staticmethod
    def identify_shape(contour: np.ndarray) -> str:
        """
        Approximates the contour to a polygon and identifies the shape
        based on the number of vertices.
        """
        perimeter = cv2.arcLength(contour, True)
        # Approximation accuracy: 2% of perimeter is a standard heuristic
        approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
        
        num_vertices = len(approx)
        
        if num_vertices == 3:
            return "Triangle"
        elif num_vertices == 4:
            # Check aspect ratio to distinguish Square vs Rectangle
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h
            # Allow 5% deviation for a square
            if 0.95 <= aspect_ratio <= 1.05:
                return "Square"
            else:
                return "Rectangle"
        elif num_vertices == 5:
            return "Pentagon"
        else:
            # If many vertices, assume it's a circle (or close to it)
            return "Circle"
    
    @staticmethod
    def get_contour_approx(contour: np.ndarray) -> np.ndarray:
        """Returns the approximated polygon for a contour."""
        perimeter = cv2.arcLength(contour, True)
        return cv2.approxPolyDP(contour, 0.04 * perimeter, True)
