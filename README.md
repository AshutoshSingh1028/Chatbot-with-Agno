---
title: Chatbot-with-Tools
emoji: 🐳
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 8501
pinned: false
---

# Chatbot with Tools

This project is a **multi-functional chatbot** built with Streamlit, designed to handle a variety of tasks ranging from simple conversations to advanced utilities. It combines contextual memory, external search, text summarization, and travel planning in one interface.

### Features

- **Basic Chatbot**: Casual conversation with contextual memory.
- **Search Functionality**: Query the web for up-to-date information.
- **Summarize from Link**: Input a URL and receive a concise summary of the content.
- **Travel Planner**: Generate travel itineraries and recommendations.


### Deployment

- Hosted on **Hugging Face Spaces**: [Chatbot with Tools](https://huggingface.co/spaces/astoast/Chatbot_with_tools)


### Setup Instructions

1. **Clone the repository:**

```bash
git clone <https://github.com/AshutoshSingh1028/Chatbot-with-Agno>
cd <your-repo-folder>
```

2. **Create and activate a virtual environment (recommended):**

```bash
python3.12 -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file** in the root directory with the following keys:

```
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
EXA_API_KEY=your_exa_key
```

5. **Run the app locally:**

```bash
streamlit run main.py
```

6. **Access it in your browser at**: `http://localhost:8501`

### Notes

- Make sure to use valid API keys in your `.env` file for full functionality.
- Contextual memory will reset when the app restarts. You may configure a custom database for persistent memory.
