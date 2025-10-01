from agno.agent import Agent
from agno.models.groq import Groq
from src.tools.search_tool import duckduckgo_search

# Create agent with custom tool
agent = Agent(
    model=Groq(id="gemma2-9b-it"),
    description="""You are an AI assistant that carefully looks at the user input and decides when to call the relevant tool. If not tool is needed, you respond directly.\
    Always use the search tool when the user query requires up-to-date information or web search.""",
    tools=[duckduckgo_search],
    markdown=True
)
