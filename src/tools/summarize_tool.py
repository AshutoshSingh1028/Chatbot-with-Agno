import requests
from bs4 import BeautifulSoup
from agno.agent import Agent
from agno.models.groq import Groq

def summarize_article(url: str) -> str:
    """Scrape and summarize any news article or blog post in exactly 3 sentences.
    
    Args:
        url (str): The URL of the article to summarize
        
    Returns:
        str: A 3-sentence summary of the article
    """
    try:
        # Scrape the article
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove unwanted elements
        for element in soup(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()
        
        # Extract main content
        content = ""
        for tag in soup.find_all(['p', 'h1', 'h2', 'h3']):
            content += tag.get_text() + " "
        
        if not content.strip():
            return "Could not extract content from the article."
        
        # Use LLM to summarize in exactly 3 sentences

        agent = Agent(
            model=Groq(id="openai/gpt-oss-20b"),
            description="You are an AI assistant that summarizes articles concisely in exactly 3 sentences.",
            instructions="Summarize the article in exactly 3 sentences, capturing the main points clearly and concisely.",
            markdown=False
        )
        
        summary = agent.run(f"Summarize the following article in exactly 3 sentences:\n\n{content}")
        return summary.content
        
    except Exception as e:
        return f"Error processing article: {str(e)}"
