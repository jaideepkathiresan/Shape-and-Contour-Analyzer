import streamlit as st
from src.models import ProcessingConfig

def render_sidebar() -> ProcessingConfig:
    """
    Renders the sidebar configuration panel and returns the config object.
    """
    st.sidebar.markdown(
        """
        <style>
        .sidebar-content {
            background-color: var(--bg-gradient-start);
        }
        /* Slider Component Theme Customization */
        div[data-baseweb="slider"] div[data-testid="stTickBar"] {
             background: #f0e68c;
        }
        div[data-baseweb="slider"] div[role="slider"] {
            background-color: #DAA520 !important;
            box-shadow: 0 0 10px rgba(218, 165, 32, 0.5);
        }
        .stSlider > div > div > div > div {
            background-color: #DAA520;
        }
        /* Sidebar Header Typography */
        .css-10trblm {
            color: #B8860B;
        }
        
        /* Author Card Class for Adaptation */
        .author-card-style {
            background: var(--card-bg);
            padding: 0.8rem;
            border-radius: 10px;
            border: 1px solid var(--card-border);
            margin-bottom: 0.8rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 2px 5px var(--card-shadow-color);
            color: var(--text-primary);
        }
        .author-card-style:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(184, 134, 11, 0.2);
        }
        .author-card-style svg {
            fill: var(--text-primary);
        }
        </style>
        """, 
        unsafe_allow_html=True
    )
    st.sidebar.title("Parameters")
    
    st.sidebar.markdown("### Edge Detection Settings")
    t1 = st.sidebar.slider("Lower Threshold (Hysteresis)", 0, 255, 50, help="Lower bound for edge detection.")
    t2 = st.sidebar.slider("Upper Threshold (Hysteresis)", 0, 255, 150, help="Upper bound for edge detection.")
    
    st.sidebar.markdown("### Noise Reduction")
    k_size = st.sidebar.slider("Blur Kernel Size", 1, 15, 5, step=2, help="Smoothing kernel size to reduce noise.")
    
    st.sidebar.markdown("### Shape Filtering")
    # Using number input for precision
    min_area = st.sidebar.number_input("Minimum Area (px)", value=100.0, step=100.0)
    max_area = st.sidebar.number_input("Maximum Area (px)", value=50000.0, step=500.0)
    
    st.sidebar.markdown("---")
    st.sidebar.caption("Adjust parameters to fine-tune detection accuracy.")
    
    # Credits and Attribution Section
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        <div style="text-align: center; margin-top: 1rem;">
            <h4 style="color: #B8860B; font-family: 'Playfair Display', serif; margin-bottom: 1rem;">Created By</h4>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Reusable Attribution Component
    def author_card(name, link):
        return f"""
        <a href="{link}" target="_blank" style="text-decoration: none; color: inherit; display: block;">
            <div class="author-card-style">
                <span style="font-weight: 600; font-size: 0.9rem;">{name}</span>
                <svg viewBox="0 0 24 24" width="20" height="20">
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
            </div>
        </a>
        """

    st.sidebar.markdown(author_card("Jaideep Vishnu Kathiresan", "https://github.com/jaideepkathiresan"), unsafe_allow_html=True)
    
    return ProcessingConfig(
        canny_threshold1=t1,
        canny_threshold2=t2,
        min_area=min_area,
        max_area=max_area,
        gaussian_kernel=k_size
    )
