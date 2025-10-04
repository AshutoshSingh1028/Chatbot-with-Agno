from agno.agent import Agent
from agno.models.groq import Groq
from src.Agent.Agent import agent
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

# --- Custom CSS ---
st.markdown("""
	<style>
	body, .stApp {
		background: #18181b !important;
		color: #e5e7eb !important;
	}
	.stTextInput > div > div > input {
		background: #23232a !important;
		color: #e5e7eb !important;
		border: 1px solid #333;
		border-radius: 8px;
		padding: 10px;
		font-size: 1.1rem;
	}
	.stButton > button {
		background: linear-gradient(90deg, #6366f1 0%, #0ea5e9 100%) !important;
		color: #fff !important;
		border: none;
		border-radius: 8px;
		padding: 10px 24px;
		font-size: 1.1rem;
		font-weight: 600;
		box-shadow: 0 2px 8px #0002;
		transition: background 0.2s;
	}
	.stButton > button:hover {
		background: linear-gradient(90deg, #0ea5e9 0%, #6366f1 100%) !important;
	}
	.stMarkdown, .stSpinner, .stTextInput, .stButton {
		color: #e5e7eb !important;
	}
	.stSpinner > div > div {
		color: #a5b4fc !important;
	}
	.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
		color: #a5b4fc !important;
	}
	.stMarkdown strong {
		color: #38bdf8 !important;
	}
	.stMarkdown p {
		color: #e5e7eb !important;
		font-size: 1.1rem;
	}
	</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align:center; font-weight:700; letter-spacing:1px; margin-bottom: 1.5rem; color:#a5b4fc;'>Multitool AI Chatbot</h1>
""", unsafe_allow_html=True)

# Sidebar with professional features description
st.sidebar.markdown("""
<div style='color:#a5b4fc; font-size:1.2rem; font-weight:600; margin-bottom:0.5rem;'>Capabilities</div>
<div style='color:#e5e7eb; font-size:1.05rem;'>
An advanced conversational AI assistant equipped with integrated tools:
<ul style='margin-top:0.5rem; margin-bottom:0.5rem;'>
	<li>Search Tool</li>
	<li>Text Summarization</li>
	<li>Travel Planning Assistance</li>
	<li>General Chat and Q&A</li>
</ul>
Delivering intelligent, multi-functional support for a variety of user needs.
</div>
""", unsafe_allow_html=True)

with st.form("chat_form", clear_on_submit=True):
	user_input = st.text_input(
		"Your message",  # Non-empty label for accessibility
		placeholder="Type your message and press Enter...",
		key="user_input",
		label_visibility="collapsed"
	)
	submitted = st.form_submit_button("Send")

if "messages" not in st.session_state:
    st.session_state.messages = []

if submitted and user_input:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        response = agent.run(user_input)

    # Show assistant response
    with st.chat_message("assistant"):
        # Prefer markdown; fallback to write
        try:
            st.markdown(response.content)
        except Exception:
            st.write(response.content)
    st.session_state.messages.append({"role": "assistant", "content": response.content})

