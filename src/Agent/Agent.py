from agno.agent import Agent
from agno.db.in_memory import InMemoryDb
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from agno.tools.exa import ExaTools
from src.tools.search_tool import duckduckgo_search
from src.tools.summarize_tool import summarize_article
from src.tools.travel_agent import FinanceToolkit
import os
from dotenv import load_dotenv
load_dotenv()


os.environ['TAVILY_API_KEY'] = os.getenv("TAVILY_API_KEY")
os.environ['EXA_API_KEY'] = os.getenv("EXA_API_KEY")


# Create agent with custom tool
agent = Agent(
    model=Groq(id="qwen/qwen3-32b"),
    db=InMemoryDb(),
    description="You are an AI assistant that carefully looks at the user input and decides when to call the relevant tool. You never assume the tools response is an error. The tools is always correct and you tell what the tool returns",
    instructions="If the relevant tool is required then always call it it. If not tool is needed, you respond directly.\
    Always use the exatools search tool when the user query requires up-to-date information or web search. Never call exatools when the user asks for summarization or travel plans.\
    Always use the summarize tool when the user query asks for a summary of a news article or blog post. Respond in exactly n sentences when summarizing where n is the number specified by the user.\
    Always use the financetoolkit when the query is related to travel and expenses.",
    add_history_to_context=True,
    tools=[ExaTools(), TavilyTools(), summarize_article, FinanceToolkit()],
    markdown=True
)
