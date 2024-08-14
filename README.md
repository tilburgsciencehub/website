# Tilburg Science Hub 

Tilburg Science Hub (TSH) is an open-source online resource that helps individual researchers, data scientists, and teams to efficiently carry out data- and computation-intensive projects. It provides information about workflow and data management and tutorials that teach researchers how to organize and document their data and code, so the research becomes sustainable and reproducible. This in turn leads to time savings and transparency in the process.

We provide the tools and guidance to be in control and save time in your empirical research projects.

**Visit us now at [tilburgsciencehub.com](https://tilburgsciencehub.com)!**

## Why was Tilburg Science Hub (TSH) developed?
We see two major reasons why it pays off to use professional tools to carry out empirical projects. First, the initial investment pays off very quickly. There are many tools that are tremendously helpful and many things can be automated, which also helps to avoid errors. Second, it increases transparency and contributes to reaching the goal of making science reproducible.

## Our pillars

### Conventions make the difference
Learn to write clean code, use conventions and version control to catch mistakes easily, make your work future-proof, and allow others to quickly review it.

### Onboarding made easy
Learn how to make teamwork exciting, not only efficient! Use SCRUM and collaboration tools to assign roles, manage tasks, and define milestones so that nobody is left behind.

### Automate your project
Learn to automate your research workflow. Don't waste time manually running each step. Let your computer take care of it for you, while you can work on something else and don't just wait behind a screen.

### Scale it up if you need more power
When the going gets tough, the tough get cloud computing. Learn to quickly resume your work running instances on remote servers.

## What does TSH offer?
Many of us face the same dilemma. We know that a small investment will have big returns, but we put off making it because we lack the time to make it now. TSH makes it easier to make this investment now by providing:

- information about all one needs to know to get started
- tutorials
- example workflows
- starter code

## Meta-Information
*   Maintainers: Hannes Datta (`@hannesdatta`), Tobias Klein (`@kleintob`)
*   Tilburg University, [Tilburg School of Economics and Management](https://www.tilburguniversity.edu/about/schools/economics-and-management)
*   Current version of website: [https://tilburgsciencehub.com](https://tilburgsciencehub.com)

## Contributing to this site

Tilburg Science Hub is an open source project,
and we welcome contributions of all kinds: new content,
fixes to the existing material, bug reports,
and reviews of proposed changes are all welcome.

* See the contributing guide [here](https://tilburgsciencehub.com/contribute/).
* Check out our [styling and writing guidelines](https://tilburgsciencehub.com/topics/more-tutorials/contribute-to-tilburg-science-hub/style-guide/).
* By contributing you agree to abide by the [Code of Conduct](https://tilburgsciencehub.com/topics/more-tutorials/contribute-to-tilburg-science-hub/code-of-conduct/).

### Automatically Running the Website

The easiest and recommended way to run Tilburg Science Hub is by using Docker.

- Install Docker and clone this repository.
- Open the terminal at the repository's root directory and run the following commands: `docker compose build` and `docker compose up`. Use the flag `-d` to run `docker compose up -d` in a detached state (so you can do something else after it has started)
- Wait a bit for the website to be launched. If the process breaks, you likely don't have sufficient memory.
- Once docker has been launched, you can access the website locally at `http://localhost:8070`.
- Press Ctrl + C in the terminal to quit.

### Automatically updating the site using Cron

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

### Manually Running the Website

#### Install Packages
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

#### Content To Database

To create the database with all necessary data, simply go to the root folder and run the following command:

```python3 content_to_db.py```

#### Start Up Flask Application
After successfully creating the database, you are ready to start up the flask application. You can dockerize the application as shown in the beginning of this README.md file or run the following command in the root folder:

`flask run`


## Any questions?
Feel free to reach out to us at [tsh@tilburguniversity.edu](mailto:tsh@tilburguniversity.edu).

## License

Text and materials are licensed under a Creative Commons CC-BY-NC-SA license. The license allows you to copy, remix and redistribute any of our publicly available materials, under the condition that you attribute the work (details in the license) and do not make profits from it. More information is available [here](https://tilburgsciencehub.com/about/#license).

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />

This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.


