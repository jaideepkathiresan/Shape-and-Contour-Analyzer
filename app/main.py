import streamlit as st
import sys
import os

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.ui.sidebar import render_sidebar
from app.ui.dashboard import render_dashboard

# Page Configuration
st.set_page_config(
    page_title="Shape Analyzer",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Core Global Styles and Custom Animations
    # Core Global Styles and Custom Animations
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@400;700&display=swap');
        
        /* 
           THEME CONFIGURATION
           Using CSS variables to handle Light/Dark mode switching automatically.
        */
        :root {
            /* Light Mode Defaults */
            --bg-gradient-start: rgb(255, 252, 236);
            --bg-gradient-end: rgb(255, 255, 255);
            --text-primary: #202124;
            --text-secondary: #5f6368;
            --card-bg: #ffffff;
            --card-border: rgba(218, 165, 32, 0.3);
            --card-shadow-color: rgba(0,0,0,0.05);
            --gold-primary: #B8860B;
            --gold-accent: #FFD700;
            --uploader-bg: #fffbf0;
            --metric-label: #555;
            --input-border: #DAA520;
        }

        @media (prefers-color-scheme: dark) {
            :root {
                /* Dark Mode Overrides */
                --bg-gradient-start: #1a1a1a; 
                --bg-gradient-end: #0e0e0e; 
                --text-primary: #e8eaed;
                --text-secondary: #9aa0a6;
                --card-bg: #1e1e1e;
                --card-border: rgba(218, 165, 32, 0.5);
                --card-shadow-color: rgba(0,0,0,0.5);
                --gold-primary: #FFD700; /* Lighter gold for contrast */
                --gold-accent: #B8860B;
                --uploader-bg: #2d2d2d;
                --metric-label: #b0b0b0;
                --input-border: #8a6e2f;
            }
        }
        
        html, body, [class*="css"] {
            font-family: 'Lato', sans-serif;
            color: var(--text-primary);
        }
        
        .main {
            background: radial-gradient(circle at 10% 20%, var(--bg-gradient-start) 0%, var(--bg-gradient-end) 90%);
        }
        
        h1 {
            font-family: 'Playfair Display', serif;
            font-size: 3.5rem;
            font-weight: 700;
            background: linear-gradient(45deg, var(--gold-primary), var(--gold-accent), #cfb53b, var(--gold-primary));
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradient_anim 8s ease infinite;
            margin-bottom: 0.5rem;
        }
        
        h2, h3 {
            font-family: 'Playfair Display', serif;
            color: var(--gold-primary); /* Adapted gold color */
        }

        @keyframes gradient_anim {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Button Styles */
        .stButton>button {
            position: relative;
            background-image: linear-gradient(to right, #B8860B 0%, #F0E68C 51%, #B8860B 100%);
            margin: 10px;
            padding: 0.8rem 2.5rem;
            text-align: center;
            text-transform: uppercase;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            background-size: 200% auto;
            color: white; /* Buttons stay white text on gold background */       
            box-shadow: 0 4px 15px rgba(184, 134, 11, 0.3);
            border-radius: 50px;
            border: none;
            font-weight: 700;
            letter-spacing: 1px;
            overflow: hidden;
            z-index: 1;
        }

        .stButton>button:hover {
            background-position: right center;
            color: #fff;
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 10px 25px rgba(212, 175, 55, 0.6);
        }
        
        .stButton>button:active {
            transform: translateY(1px);
            box-shadow: 0 2px 10px rgba(184, 134, 11, 0.4);
        }

        /* 
           Shared UI Component: Interactive Card with Animated Border Gradient
           Applied to: Custom Cards, DataFrames, and Images
        */
        .interactive-card, 
        div[data-testid="stDataFrame"],
        div[data-testid="stImage"] img {
            position: relative;
            background: var(--card-bg); /* Adaptive background */
            border-radius: 16px;
            padding: 1.5rem !important; 
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px var(--card-shadow-color); /* Adaptive shadow */
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border: 1px solid transparent; 
        }

        /* The Animated Gradient Border Pseudo-element */
        .interactive-card::before,
        div[data-testid="stDataFrame"]::before,
        div[data-testid="stImage"] img::before {
            content: "";
            position: absolute;
            inset: 0;
            border-radius: 16px; 
            padding: 2px; 
            background: linear-gradient(90deg, #B8860B, transparent, #FFD700, transparent, #B8860B); 
            background-size: 200% 100%;
            -webkit-mask: 
                linear-gradient(#fff 0 0) content-box, 
                linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            
            opacity: 0.5; 
            transition: opacity 0.3s ease;
            pointer-events: none; 
        }
        
        /* Hover Interaction */
        .interactive-card:hover,
        div[data-testid="stDataFrame"]:hover,
        div[data-testid="stImage"] img:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(184, 134, 11, 0.15);
        }

        .interactive-card:hover::before,
        div[data-testid="stDataFrame"]:hover::before {
            opacity: 1;
            animation: border_flow 2s linear infinite;
        }

        @keyframes border_flow {
            0% { background-position: 0% 0%; }
            100% { background-position: 200% 0%; }
        }
        
        .interactive-card h4 {
            color: var(--gold-primary);
            font-family: 'Playfair Display', serif;
            margin-bottom: 0.5rem;
        }
        
        .interactive-card p {
            color: var(--text-secondary) !important;
        }

        /* Other UI tweaks */
        div[data-testid="stMetricValue"] {
            color: #DAA520; /* Keep gold */
            font-family: 'Playfair Display', serif;
            font-size: 2.2rem;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }
        div[data-testid="stMetricLabel"] {
            color: var(--metric-label);
            font-weight: 600;
            letter-spacing: 1px;
        }

        [data-testid='stFileUploader'] section {
            background-color: var(--uploader-bg);
            border: 2px dashed var(--input-border);
            transition: border-color 0.3s;
        }
        [data-testid='stFileUploader'] section:hover {
            border-color: #B8860B;
        }

        .header-container {
            padding: 3rem 0;
            text-align: center;
            position: relative;
            margin-bottom: 3rem;
        }
        
        .sub-header {
            font-size: 1.3rem;
            color: var(--text-secondary); /* Adaptive */
            font-style: italic;
            font-weight: 400;
        }
        </style>
    """, unsafe_allow_html=True)

    # Navigation / Credits Section
    # Navigation / Credits Section
    st.markdown("""
        <div style="display: flex; justify-content: flex-end; gap: 15px; margin-bottom: 0.5rem;">
            <a href="https://github.com/jaideepkathiresan" target="_blank" style="text-decoration: none; color: inherit;">
                <div class="author-card-style">
                    <span style="font-weight: 600; font-size: 0.9rem;">Jaideep Vishnu Kathiresan</span>
                    <svg viewBox="0 0 24 24" width="20" height="20">
                        <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                    </svg>
                </div>
        </div>
    """, unsafe_allow_html=True)

    # Header Section
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    st.title("Shape & Contour Analyzer")
    st.markdown('<p class="sub-header">Geometric Analysis & Feature Extraction</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Render Sidebar
    config = render_sidebar()

    # Main File Upload Interface
    st.markdown("### Input Data")
    uploaded_file = st.file_uploader("Upload an image for analysis", type=['png', 'jpg', 'jpeg', 'bmp'], label_visibility="collapsed")

    if uploaded_file is not None:
        render_dashboard(uploaded_file, config)
    else:
        # Empty State Display
        st.markdown("""
        <div class="interactive-card" style="text-align: center;">
            <h3 style="color: #DAA520; margin-bottom: 1rem; font-family: 'Playfair Display', serif;">Begin Analysis</h3>
            <p style="color: #666; margin-bottom: 0;">Upload a high-quality image to extract geometric insights.</p>
        </div>
        """, unsafe_allow_html=True)

        # Application Capabilities Overview
        st.markdown("---")
        st.subheader("System Capabilities")
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.markdown("""
            <div class="interactive-card">
                <h4>Shape Detection</h4>
                <p style="font-size: 0.9rem; color: #666;">Identifies standard geometric polygons with high precision.</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class="interactive-card">
                <h4>Feature Extraction</h4>
                <p style="font-size: 0.9rem; color: #666;">Computes area, perimeter, and centroid coordinates.</p>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown("""
            <div class="interactive-card">
                <h4>Contour Analysis</h4>
                <p style="font-size: 0.9rem; color: #666;">Advanced boundary tracing and visualization overlays.</p>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
