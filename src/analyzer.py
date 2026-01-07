import cv2
import numpy as np
from typing import List
from .models import ShapeInfo, ProcessingConfig
from .processors import ImageProcessor
from .detectors import ShapeDetector

class ImageAnalyzer:
    """Orchestrator for the analysis pipeline."""

    def __init__(self, config: ProcessingConfig):
        self.config = config
        self.processor = ImageProcessor()
        self.detector = ShapeDetector()

    def analyze(self, image: np.ndarray) -> List[ShapeInfo]:
        """
        Full pipeline: Preprocess -> Find Contours -> Filter -> Identify -> Return Results.
        """
        # 1. Preprocessing
        gray = self.processor.to_grayscale(image)
        blur = self.processor.apply_blur(gray, self.config.gaussian_kernel)
        edges = self.processor.detect_edges(
            blur, self.config.canny_threshold1, self.config.canny_threshold2
        )

        # 2. Contour Extraction
        contours = self.processor.get_contours(edges)

        results = []
        for cnt in contours:
            # 3. Filtering
            area = cv2.contourArea(cnt)
            if area < self.config.min_area or area > self.config.max_area:
                continue

            # 4. Geometry Calculations
            perimeter = cv2.arcLength(cnt, True)
            M = cv2.moments(cnt)
            
            # Use small epsilon to avoid division by zero
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
            else:
                cx, cy = 0, 0
            
            centroid = (cx, cy)
            
            # 5. Identification
            shape_type = self.detector.identify_shape(cnt)
            approx = self.detector.get_contour_approx(cnt)

            results.append(ShapeInfo(
                shape_type=shape_type,
                area=area,
                perimeter=perimeter,
                centroid=centroid,
                contour=cnt,
                approx_contour=approx
            ))
            
        return results
