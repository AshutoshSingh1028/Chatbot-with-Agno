import requests
from bs4 import BeautifulSoup
from agno.agent import Agent
from agno.models.groq import Groq

def summarize_article(url: str, n: int) -> str:
    """Scrape and summarize any news article or blog post in exactly n sentences. If the user does not specify the number of sentences, summarize in exactly 3 sentences.\
       Always number the sentences in the summary. 
    
    Args:
        url (str): The URL of the article to summarize   
        
    Returns:
        str: The content of the article or an error message.
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
        
        return content.strip()
        
    except Exception as e:
        return f"Error processing article: {str(e)}"
