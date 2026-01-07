import cv2
import numpy as np
from typing import List
from src.models import ShapeInfo

def draw_results(image: np.ndarray, shapes: List[ShapeInfo]) -> np.ndarray:
    """
    Draws contours, shape names, and centroids on a copy of the image.
    """
    # Create a copy to avoid mutating original
    output = image.copy()
    
    for shape in shapes:
        # Draw Contour
        # Green color for contour, thickness 2
        cv2.drawContours(output, [shape.approx_contour], -1, (0, 255, 0), 2)
        
        # Draw Centroid
        cv2.circle(output, shape.centroid, 5, (255, 0, 0), -1)
        
        # Put Text Label (Shape Name + Area)
        label = f"{shape.shape_type} A:{int(shape.area)}"
        
        # Dynamic text placement
        text_x = shape.centroid[0] - 20
        text_y = shape.centroid[1] - 20
        
        cv2.putText(
            output, 
            label, 
            (text_x, text_y), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.5, 
            (0, 0, 0), # Black border for readability
            3
        )
        cv2.putText(
            output, 
            label, 
            (text_x, text_y), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.5, 
            (255, 255, 255), # White text
            1
        )
        
    return output
