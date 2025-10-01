import json
from typing import Optional
from agno.agent import Agent
from ddgs import DDGS

def duckduckgo_search(query: str) -> str:
    """Search DuckDuckGo and return only the top 2 results.
    
    Args:
        query (str): The search query
        
    Returns:
        str: JSON formatted search results (top 2 only)
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=2))
            return json.dumps(results, indent=2)
    except Exception as e:
        return f"Search failed: {str(e)}"
    
