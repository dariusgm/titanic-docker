# Base image
FROM python:3.10 AS base

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy python files
COPY *.py .

FROM base AS api
# Expose port for Flask API
EXPOSE 5000
# Run the Flask API
CMD ["python", "/app/api.py"]

FROM base AS app
# Run the streamlit frontend app
EXPOSE 5050
CMD ["streamlit", "run", "app.py", "--server.port", "5050", "--browser.serverAddress", "0.0.0.0"]
