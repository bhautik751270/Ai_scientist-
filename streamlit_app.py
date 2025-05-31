# streamlit_app.py

import streamlit as st
from agents.planner import plan_research

st.set_page_config(page_title="AI Scientist Lab", page_icon="🧠")

st.title("🧪 Self-Improving AI Scientist")
st.subheader("Generate a research plan with Groq + LLaMA3")

# Input from user
topic = st.text_input("Enter your research topic:")

if topic:
    with st.spinner("Planning your research..."):
        subtasks = plan_research(topic)
    
    st.success("Here is your AI-generated research plan:")
    for task in subtasks:
        st.markdown(f"✅ {task}")
