# Tilburg Science Hub (Flask)

This is the repository thats hosts the flask application for Tilburg Science Hub.

## Automatically Running the Website

The easiest way to run Tilburg Science Hub is using Docker.

- Install Docker and clone this repository.
- Open the terminal at the repository's root directory and run the following commands: `docker compose build` and `docker compose up`. Use the flag `-d` to run `docker compose up -d` in detached state (so you can do something else after it has started)
- Wait a bit for the website to be launched. If the process breaks, you likely dont' have sufficient memory.
- Once docker has been launched, you can access the website locally at `http://localhost:8000`.
- Press Ctrl + C in the terminal to quit.

## Manually Running the Website

### Install Packages
```
pip install Flask-SQLAlchemy
pip install SQLAlchemy
pip install beautifulsoup4
pip install nltk
pip install markdown
pip install Flask-Assets
pip install google-api-python-client
```

If problems arrive with scss, please install sass:

```
npm install sass
```

### Content To Database

To create the database with all necessary data, simply go to the root folder and run the following command:

```python3 content_to_db.py```

### Start Up Flask Application
After successfully creating the database, you are ready to start up the flask application. To do so run the following command in the root folder:

`flask run`
