from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from src.tools.search_tool import duckduckgo_search
from src.tools.summarize_tool import summarize_article
import os
from dotenv import load_dotenv
load_dotenv()


os.environ['TAVILY_API_KEY'] = os.getenv("TAVILY_API_KEY")


# Create agent with custom tool
agent = Agent(
    model=Groq(id="qwen/qwen3-32b"),
    description="You are an AI assistant that carefully looks at the user input and decides when to call the relevant tool.",
    instructions="If the relevant tool is required then always call it it. If not tool is needed, you respond directly.\
    Always use the search tool when the user query requires up-to-date information or web search.\
    Always use the summarize tool when the user query asks for a summary of a news article or blog post. Respond in exactly 3 sentences when summarizing.",
    tools=[TavilyTools(search_depth='advanced'), summarize_article],
    markdown=True
)
