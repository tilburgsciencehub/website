# Tilburg Science Hub (Flask)

This is the repository thats hosts the flask application for Tilburg Science Hub.

## Automatically Running the Website

The easiest and recommended way to run Tilburg Science Hub is by using Docker.

- Install Docker and clone this repository.
- Open the terminal at the repository's root directory and run the following commands: `docker compose build` and `docker compose up`. Use the flag `-d` to run `docker compose up -d` in a detached state (so you can do something else after it has started)
- Wait a bit for the website to be launched. If the process breaks, you likely don't have sufficient memory.
- Once docker has been launched, you can access the website locally at `http://localhost:8070`.
- Press Ctrl + C in the terminal to quit.

## Automatically updating the site using Cron

The file `update_and_restart.sh` automatically runs the deployment on the server. It can be scheduled using a cron job so that the website automatically updates.

1. **Open the Crontab File**:
   Open the crontab file for editing by running the following command:
   ```bash
   crontab -e
   ```

2. **Add the Cron Job**:
   Add a new line at the end of the file to schedule the script. The following example schedules the script to run every day at midnight:
   ```bash
   0 0 * * * /home/ubuntu/update_and_restart.sh >> /home/ubuntu/update_and_restart.log 2>&1
   ```

   - **0 0 * * ***: This specifies that the script should run at midnight (00:00) every day.
   
3. **Save and Exit**:
   Save the changes and exit the editor. The cron daemon will now schedule the script to run at the specified times.

### Additional Scheduling Examples

- **Every 5 Minutes**:
  ```bash
  */5 * * * * /path/to/update_and_restart.sh >> /path/to/update_and_restart.log 2>&1
  ```

- **Every Hour**:
  ```bash
  0 * * * * /path/to/update_and_restart.sh >> /path/to/update_and_restart.log 2>&1
  ```

- **Every Sunday at 2 AM**:
  ```bash
  0 2 * * 0 /path/to/update_and_restart.sh >> /path/to/update_and_restart.log 2>&1
  ```

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
After successfully creating the database, you are ready to start up the flask application. You can dockerize the application as shown in the beginning of this README.md file or run the following command in the root folder:

`flask run`
