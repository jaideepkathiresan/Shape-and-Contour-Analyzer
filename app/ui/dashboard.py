import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from typing import List
from src.analyzer import ImageAnalyzer
from src.models import ShapeInfo, ProcessingConfig
from .visuals import draw_results

def render_dashboard(uploaded_file, config: ProcessingConfig):
    """
    Main dashboard view.
    """
    # Load Image
    image_pil = Image.open(uploaded_file)
    image_np = np.array(image_pil.convert('RGB')) 
    # Convert RGB to BGR for OpenCV
    image_bgr = image_np[:, :, ::-1].copy()

    # Process
    analyzer = ImageAnalyzer(config)
    results: List[ShapeInfo] = analyzer.analyze(image_bgr)
    
    # Visualize
    result_image_bgr = draw_results(image_bgr, results)
    # Convert back to RGB for Streamlit
    result_image_rgb = result_image_bgr[:, :, ::-1]

    # Key Performance Indicators (KPIs) Display
    st.markdown("### Analysis Results")
    
    unique_shapes = set(s.shape_type for s in results)
    largest_shape = max(results, key=lambda x: x.area) if results else None
    largest_text = f"{largest_shape.shape_type}" if largest_shape else "N/A"
    
    # Aggregated Metrics Container
    st.markdown(f"""
    <div class="interactive-card">
        <div style="display: flex; justify-content: space-around; align-items: center; text-align: center;">
            <div>
                <div style="font-size: 0.9rem; color: #555; text-transform: uppercase; letter-spacing: 1px;">Total Objects</div>
                <div style="font-size: 2.2rem; font-family: 'Playfair Display', serif; color: #DAA520; font-weight: 700;">{len(results)}</div>
            </div>
            <div style="border-left: 1px solid #ddd; height: 50px;"></div>
            <div>
                <div style="font-size: 0.9rem; color: #555; text-transform: uppercase; letter-spacing: 1px;">Unique Shapes</div>
                <div style="font-size: 2.2rem; font-family: 'Playfair Display', serif; color: #DAA520; font-weight: 700;">{len(unique_shapes)}</div>
            </div>
            <div style="border-left: 1px solid #ddd; height: 50px;"></div>
            <div>
                <div style="font-size: 0.9rem; color: #555; text-transform: uppercase; letter-spacing: 1px;">Primary Shape</div>
                <div style="font-size: 2.2rem; font-family: 'Playfair Display', serif; color: #DAA520; font-weight: 700;">{largest_text}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Image Visualization
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Image")
        # Render Images within styled container
        st.image(image_pil, use_container_width=True)
        
    with col2:
        st.subheader("Detected Shapes")
        st.image(result_image_rgb, use_container_width=True)

    # Detailed Stats Table
    if results:
        st.markdown("### Detailed Statistics")
        data = []
        for i, r in enumerate(results):
            data.append({
                "ID": i+1,
                "Type": r.shape_type,
                "Area (px²)": f"{r.area:.1f}",
                "Perimeter (px)": f"{r.perimeter:.1f}",
                "Centroid (X,Y)": str(r.centroid)
            })
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No shapes detected. Try adjusting the thresholds in the sidebar.")
