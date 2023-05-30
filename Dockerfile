# Base image
FROM python:3.10 AS base

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY app.py .


FROM base AS api
# Expose port for Flask API
EXPOSE 8000
# Run the Streamlit app and Flask API
CMD ["python", "api.py"]

FROM base AS train
CMD ["python", "train.py"]

FROM base AS app
CMD ["streamlit", "run", "app.py"]
