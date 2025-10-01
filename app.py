from agno.agent import Agent
from agno.models.groq import Groq
from src.Agent.Agent import agent
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

agent.print_response("where did i ask to plan the trip for first?")