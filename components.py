import streamlit as st
from config import PRIMARY_COLOR, TEXT_COLOR, SECONDARY_BG
from data import job_data

def render_header():
    st.markdown(
        '<div class="profile-section">'
        f'<span style="background-color: {PRIMARY_COLOR}; color: black; padding: 5px 10px; border-radius: 15px;">Profile</span> '
        f'<span style="color: {TEXT_COLOR};">Kunal</span>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div style="margin-top: 50px;"></div>', unsafe_allow_html=True)

def render_sidebar():
    with st.sidebar:
        st.markdown('<div class="app-header">JobDekho</div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(f'<div style="color: {PRIMARY_COLOR}; font-weight: bold;">Dashboard</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="color: {TEXT_COLOR};">Jobs</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="color: {TEXT_COLOR};">Skills</div>', unsafe_allow_html=True)

def render_skills_input():
    all_skills = sorted(list(set([skill for job in job_data for skill in job["skills"]])))
    
    st.markdown(f'<div style="background-color: {SECONDARY_BG}; padding: 20px; border-radius: 10px; margin-bottom: 20px;">', unsafe_allow_html=True)
    user_skills = st.multiselect("Enter your skills", all_skills)
    st.markdown('</div>', unsafe_allow_html=True)

    if user_skills:
        st.markdown('<div class="user-skills-section">', unsafe_allow_html=True)
        skills_html = "".join([f'<span class="user-skill-tag">{skill}</span> ' for skill in user_skills])
        st.markdown(skills_html, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    return user_skills

def render_job_cards(job_data, user_skills):
    if user_skills:
        filtered_jobs = []
        for job in job_data:
            matching_skills = [skill for skill in user_skills if skill in job["skills"]]
            if matching_skills:
                match_percentage = int((len(matching_skills) / len(job["skills"])) * 100)
                job_copy = job.copy()
                job_copy["match_percentage"] = min(match_percentage, 100)
                filtered_jobs.append(job_copy)
        filtered_jobs = sorted(filtered_jobs, key=lambda x: x["match_percentage"], reverse=True)
    else:
        filtered_jobs = job_data

    st.markdown('<div class="section-header">Recommended Jobs</div>', unsafe_allow_html=True)
    cols = st.columns(3)

    for i, job in enumerate(filtered_jobs):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="job-card">
                <div class="job-title">{job["title"]}</div>
                <div>{"".join([f'<span class="skill-tag">{skill}</span> ' for skill in job["skills"]])}</div>
                <div class="match-percentage">{job["match_percentage"]}% Match</div>
            </div>
            """, unsafe_allow_html=True)

    if user_skills and not filtered_jobs:
        st.info("No jobs match your skills. Try adding more skills or different ones.")