FROM python:3.8-slim as base

WORKDIR /app

RUN pip install --no-cache-dir Flask-SQLAlchemy \
    SQLAlchemy \
    beautifulsoup4 \
    nltk \
    markdown \
    Flask-Assets \
    google-api-python-client

RUN python3 content_to_db.py

COPY . . 

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]