import streamlit as st
from config import PRIMARY_COLOR, BACKGROUND_COLOR, SECONDARY_BG, TEXT_COLOR

def apply_custom_styles():
    custom_css = f"""
    <style>
        .main {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR};
        }}
        .stApp {{
            background-color: {BACKGROUND_COLOR};
        }}
        .sidebar .sidebar-content {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR};
        }}
        .css-1d391kg {{
            padding-top: 3rem;
        }}
        .job-card {{
            background-color: {SECONDARY_BG};
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 15px;
        }}
        .job-title {{
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        .skill-tag, .user-skill-tag {{
            background-color: {PRIMARY_COLOR};
            color: black;
            padding: 5px 10px;
            border-radius: 5px;
            margin-right: 5px;
            display: inline-block;
            margin-bottom: 5px;
        }}
        .match-percentage {{
            margin-top: 10px;
            color: #AAAAAA;
        }}
        .app-header, .section-header {{
            color: {PRIMARY_COLOR};
        }}
        .app-header {{
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 20px;
        }}
        .section-header {{
            font-size: 24px;
            font-weight: bold;
            margin: 20px 0;
        }}
        .user-skills-section {{
            margin: 20px 0;
        }}
        label, .stTextInput label, .stMultiSelect label {{
            color: {PRIMARY_COLOR} !important;
            font-weight: bold !important;
            font-size: 16px !important;
        }}
        .stTextInput input, .stMultiSelect input {{
            color: {TEXT_COLOR} !important;
            background-color: #2D2D2D !important;
        }}
        .profile-section {{
            position: absolute;
            top: 20px;
            right: 20px;
            z-index: 1000;
        }}
        .stMultiSelect [data-baseweb="select"] {{
            background-color: #2D2D2D;
        }}
        .stMultiSelect [data-baseweb="select"] span {{
            color: {TEXT_COLOR};
        }}
        .stButton button {{
            background-color: {PRIMARY_COLOR} !important;
            color: black !important;
            font-weight: bold !important;
        }}
        [data-baseweb="menu"] {{
            background-color: #2D2D2D !important;
        }}
        [data-baseweb="menu"] li {{
            color: {TEXT_COLOR} !important;
        }}
        [data-baseweb="menu"] li:hover {{
            background-color: #3D3D3D !important;
        }}
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)