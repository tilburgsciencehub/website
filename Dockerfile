# Use an official Python runtime as the parent image
FROM python:3.8-slim

# Set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && \
    apt-get install -y libcurl4-openssl-dev curl && \
    apt-get install -y git && \
    curl -fsSL https://deb.nodesource.com/setup_22.x -o nodesource_setup.sh && \
    bash nodesource_setup.sh && \
    apt-get install -y nodejs && \ 
    node -v && \
    find /var/*/apt -type f -delete

RUN pip install --no-cache-dir Flask-SQLAlchemy \
    SQLAlchemy \
    beautifulsoup4 \
    nltk \
    markdown \
    Flask-Assets \
    google-api-python-client \
    gunicorn \
    Pillow \
    Flask-Compress

RUN npm install -g sass

# Copy the current directory contents into the container at /app
COPY . /app/

# Create database
RUN python3 content_to_db.py

# Download nltk package
RUN python3 -c "import nltk; nltk.download('stopwords')"

# Make port 80 available to the world outside this container
EXPOSE 8080

# Run gunicorn when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--timeout", "240", "--workers", "2", "app:app"]