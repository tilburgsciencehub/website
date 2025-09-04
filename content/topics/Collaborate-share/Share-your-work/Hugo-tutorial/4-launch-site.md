---
type: "hugo-tutorial"
title: "(Part 3) Using Hugo: Create and Deploy a Static Site"
description: "Learn how to launch your site with Hugo after installation"
draft: false
weight: 4
date: 2025-07-07
author: "Harold Miesen"
---

## (Part 3) Using Hugo: Create and Deploy a Static Site

Hugo is a powerful static site generator that transforms plain text and templates into fast,
secure, and fully pre-rendered websites. Unlike dynamic sites that rely on databases, static
sites are composed of HTML files that can be easily hosted anywhere—from GitHub Pages to
cloud providers—with excellent performance and minimal maintenance.

### Step 1: Create a New Project
Start by opening a terminal window:

- Windows: open __**powershell**__
- Linux: open the __**terminal**__ application.

> The terminal starts in a default folder, but you can choose where to create your Hugo project.

Use the `cd` command to move into the folder where you'd like to store your Hugo project. For example:

__**Windows powershell**__:

```
cd ~\Documents\Websites
```
__**Linux**__

```
cd ~/Documents/Websites
```

The tilde (`~`) is a shortcut that represents your __**home directory**__—your personal user folder.

- On __**Windows**__ (powershell): `~` means something like `C:\Users\YourName`
- On __**Linux**__: `~` means something like `/home/Yourname`

So when you run `cd ~/Documents` you're navigating to the `Documents` folder inside your home directory.

You can also create a new folder first:

```
mkdir HugoProjects
cd HugoProjects
```

Create a new Hugo site by running the following command in the folder in which you want to create the site:

```
hugo new site my-hugo-site
cd my-hugo-site
```

This creates a new folder called my-hugo-site in your current directory. Hugo will place all the
starter files inside that folder.

> For example, if you're in `C:\Users\YourName\Documents\HugoProjects`, the new project will be
created at `C:\Users\YourName\Documents\HugoProjects\my-hugo-site`.

> __**TIP**__: Choose a meaningful name for your project folder. You can manage multiple Hugo sites
independently.

### Step 2: Add a Theme (Ananke)
Add the [Ananke](https://github.com/theNewDynamic/gohugo-theme-ananke) theme using Git submodules:

```
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke

```
> __**Why Ananke**__? It's a modern, responsive, and accessible theme - great for learning and
production alike.

By now, you should have a directory structure looking something like this:

```
my-hugo-site/
├── hugo.toml       # Site configuration
├── content/        # Pages
├── themes/         # Downloaded theme
├── static/         # Custom assets (images, CSS, JS)
├── layouts/        # Optional layout overrides
└── public/         # Generated output (DO NOT EDIT)
```

> The `public/` folder is regenerated with every `hugo` build. Never edit it manually.

### Step 3: Configure `hugo.toml`
Edit hugo.toml in your favorite editor and set basic site configuration by adding the
following lines:

```
baseURL = "http://localhost/"
languageCode = "en-us"
title = "My Hugo Site"
theme = "ananke"
```

__**Additional settings**__ you may want to add:
```
paginate = 10
enableRobotsTXT = true
```

If you’d like Hugo to automatically add front matter when creating new content, you can define
a default archetype.

Create a file at `archetypes/default.md`.

And add the following content:

```
---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true
---
```

- When you run a command like hugo new about.md, Hugo will use this template.
- The title will be auto-generated from the filename (e.g., about becomes About).
- The date is set to the current timestamp.
- The page will be created as a draft, which you can later publish by setting `draft: false`.

### Step 4: Run Local Server
Start the Hugo development server in __**the root**__ of your project:
```
hugo server -D
```

Visit [http://localhost:1313](http://localhost:1313) in your browser.

> - Live reload is enabled - changes are reflected immediately.
> - The -D flag in hugo server includes draft content in the local build, which is useful during
development but should be avoided in production to prevent publishing unfinished work.

### Bonus: Deploy your static site to a remote server

#### 1. Commit your project source to main
Make sure your Hugo project (including content, theme, and config files) is version-controlled:

```
git init
git add .
git commit -m "Initial commit with Hugo source files"
git remote add origin https://github.com/<your-username>/my-hugo-site.git
git branch -M main
git push -u origin main
```

> This keeps your full source code in the `main` branch.

#### 2. Build the static site
Go to the root of your project and use Hugo to generate the final website:

```
hugo --gc --minify
```

> The output will be placed in the `public/` directory. When you build a Hugo site,
> Hugo outputs all generated HTML, CSS, JS, and other assets into this 
> `public/` directory.
>
> The --gc flag in Hugo enables garbage collection: it removes unused files from the 
> output (`public/`) directory during a build, so old or orphaned files from previous
> builds don’t remain.

#### 3. Push only the contents of the public/ folder to a separate branch
You'll now push only the contents of the `public/` folder to a separate branch:

```
cd public
git init
git checkout -b deployment
git remote add origin https://github.com/<your-username>/my-hugo-site.git
git add .
git commit -m "Push contents of the public folder to a separate branch"
git push -f origin deployment
```

> __**Force push**__ – -f is intentional here to overwrite the deployment branch,
> but be aware it will replace its history completely.

#### 4. Deploy the static site to a remote server

The `public/` directory is your complete static website—you can use its contents
directly as the static content directory for a web server. For example, if you
want to serve the site using [Nginx in Docker](https://hub.docker.com/_/nginx),
simply copy the `public/` directory into the location Nginx uses for static files
(by default `/usr/share/nginx/html`). For the rest of the setup, follow the
official [Nginx Docker image and their beginner
documentation](https://www.docker.com/blog/how-to-use-the-official-nginx-docker-image/).

### Bonus: Automate Deployment
Instead of manually pushing `public/`, you can automate this with [GitHub Actions]
(https://github.com/features/actions).

You're now ready to add content to your static Hugo site and to continue to the 
[Adding content to your Hugo site](../5-add-content/),
or go back to [Hugo Tutorial: Start Here](../1-index/).
