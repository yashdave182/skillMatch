import streamlit as st
from config import PAGE_CONFIG
from styles import apply_custom_styles
from components import render_header, render_sidebar, render_skills_input, render_job_cards
from data import job_data

def main():
    # Apply page config and custom styles
    st.set_page_config(**PAGE_CONFIG)
    apply_custom_styles()
    
    # Render UI components
    render_header()
    render_sidebar()
    
    # Get user skills and render job cards
    user_skills = render_skills_input()
    render_job_cards(job_data, user_skills)

if __name__ == "__main__":
    main()