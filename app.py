from agno.agent import Agent
from agno.models.groq import Groq
from src.Agent.Agent import agent
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

st.title("Agentic AI Chatbot")
user_input = st.text_input("Ask something:")

if user_input:
	with st.spinner("Thinking..."):
		response = agent.run(user_input)
	st.markdown("**Response:**")
	st.write(response.content)