import pytest
import numpy as np
import cv2
from src.detectors import ShapeDetector

class TestShapeDetector:
    
    @staticmethod
    def _create_regular_polygon_contour(sides: int, radius: int = 50) -> np.ndarray:
        """Helper to generate a regular polygon contour centered at (100, 100)."""
        center = (100, 100)
        points = []
        for i in range(sides):
            angle = 2 * np.pi * i / sides
            x = int(center[0] + radius * np.cos(angle))
            y = int(center[1] + radius * np.sin(angle))
            points.append([x, y])
        return np.array(points, dtype=np.int32).reshape((-1, 1, 2))

    @staticmethod
    def _create_rectangle_contour(w: int, h: int) -> np.ndarray:
        return np.array([
            [0, 0], [w, 0], [w, h], [0, h]
        ], dtype=np.int32).reshape((-1, 1, 2))

    def test_triangle_detection(self):
        # Create a triangle (3 vertices)
        triangle_cnt = self._create_regular_polygon_contour(3)
        shape_type = ShapeDetector.identify_shape(triangle_cnt)
        assert shape_type == "Triangle"

    def test_square_detection(self):
        # Create a square (4 vertices, aspect ratio ~1)
        # Note: _create_rectangle_contour doesn't guarantee exact aspect ratio after approx unless points are precise
        # Let's use points directly
        square_cnt = np.array([
            [0, 0], [100, 0], [100, 100], [0, 100]
        ], dtype=np.int32).reshape((-1, 1, 2))
        
        shape_type = ShapeDetector.identify_shape(square_cnt)
        assert shape_type == "Square"

    def test_rectangle_detection(self):
        # Rectangle with different width and height
        rect_cnt = np.array([
            [0, 0], [200, 0], [200, 100], [0, 100]
        ], dtype=np.int32).reshape((-1, 1, 2))
        
        shape_type = ShapeDetector.identify_shape(rect_cnt)
        assert shape_type == "Rectangle"

    def test_pentagon_detection(self):
        pentagon_cnt = self._create_regular_polygon_contour(5)
        shape_type = ShapeDetector.identify_shape(pentagon_cnt)
        assert shape_type == "Pentagon"

    def test_circle_detection(self):
        # Circle is approximated by a polygon with many sides (e.g., 20)
        # However, approxPolyDP simplifies it. If we generate a perfect circle visually, 
        # approxPolyDP might still reduce it if epsilon is high.
        # But for 'Circle' logic in detector, it's > 5 vertices.
        # Let's create a 10-gon.
        decagon_cnt = self._create_regular_polygon_contour(10)
        shape_type = ShapeDetector.identify_shape(decagon_cnt)
        assert shape_type == "Circle"
