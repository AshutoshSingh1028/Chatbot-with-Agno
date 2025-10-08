import requests
from bs4 import BeautifulSoup
from agno.agent import Agent
from agno.models.groq import Groq

def extract_article_text(url: str) -> str:
    """Scrape any news article or blog post and return the text content."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Remove unwanted elements
        for element in soup(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()

        # Extract paragraphs and headings
        content = ""
        for tag in soup.find_all(['p', 'h1', 'h2', 'h3']):
            content += tag.get_text() + " "

        if not content.strip():
            return "Could not extract content from the article."

        return content.strip()

    except Exception as e:
        return f"Error processing article: {str(e)}"


def chunk_text(text: str, max_words: int = 500):
    """Split text into chunks of max_words words."""
    words = text.split()
    for i in range(0, len(words), max_words):
        yield " ".join(words[i:i + max_words])


def summarize_chunk(chunk: str, n: int = 3) -> str:
    """Summarize a chunk of text in exactly n numbered sentences."""
    agent = Agent(
        model=Groq(id="openai/gpt-oss-20b"),
    )

    prompt = f"Summarize the following text in exactly {n} numbered sentences:\n\n{chunk}"
    summary = agent.run(prompt)

    return summary.content.strip()


def summarize_article(url: str, n: int = 3) -> str:
    """
    Scrape and summarize any article or blog post in exactly n sentences.
    if the user does not specify n, default to 3.
    Always use pointered sentences.
    If the article is too long, summarize it in chunks and combine results.
    """
    article_text = extract_article_text(url)

    # Handle scraping errors
    if "Error" in article_text or "Could not" in article_text:
        return article_text

    # Break the text into smaller chunks
    chunks = list(chunk_text(article_text, max_words=500))

    # Summarize each chunk individually
    chunk_summaries = [summarize_chunk(chunk, n) for chunk in chunks]

    # If there are multiple chunk summaries, summarize them again
    if len(chunk_summaries) > 1:
        combined_text = " ".join(chunk_summaries)
        final_summary = summarize_chunk(combined_text, n)
    else:
        final_summary = chunk_summaries[0]

    return final_summary
