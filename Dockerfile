# Use official Python 3.12 image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files except .env and __pycache__
COPY . .

# Remove .env file if present
RUN rm -f .env

# Remove all __pycache__ directories recursively
RUN find . -type d -name "__pycache__" -exec rm -rf {} +

# Expose default Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "main.py"]