---
tutorialtitle: "Create Your Own Website in 15 Minutes"
type: "hugo-website"
indexexclude: "true"
title: "Add Some Content"
description: "Learn how to customize your Hugo website and add content to it."
keywords: "hugo, content, markdown, writing, articles"
date: 2021-01-06T22:01:14+05:30
draft: false
weight: 13
author: "Andrea Antonacci"
authorlink: "https://www.tilburguniversity.edu/staff/a-d-antonacci"
aliases:
  - /use/hugo-website
  - /add-content/hugo-website
  - /tutorials/open-education/hugo-website/add-content
---

## The `content` Folder
Now that you've set up a theme for your Hugo website, you can finally start to write some content!

Just **manually create Markdown files** using a text editor and place them in the `content` folder. The path should look something like this: `content/<CATEGORY>/<FILE>.md`. Usually, you can create as many categories as you want, but it's better to check the theme documentation.

{{% example %}}
For instance, the [About page of odcm.hannesdatta.com](https://odcm.hannesdatta.com/docs/about/) is placed inside `content/docs/about/`.
{{% /example %}}

## The Front Matter

You must always **provide some metadata** inside your content files for them to work properly, like a title and a date. For instance, a new file could start with something similar to this:
```
---
title: "My First Post"
date: 2019-03-26T08:47:11+01:00
draft: true
---

Your content goes here. You can write anything you want using the Markdown syntax.
```

What's within the `---` is called **front matter**. You can learn more about predefined and used-defined front matter variables [here](https://gohugo.io/content-management/front-matter/).

{{% tip %}}
Notice the variable `draft: true`. When the site gets built, articles set to drafts won't be deployed. Set draft to false if you want to include them in your public website.
{{% /tip %}}

## Preview Your Edits

You know how to edit your content now. Wouldn't it be great if you could preview how your articles will look like once the website gets published?

Luckily, Hugo allows you to do exactly so with a "local server". Just run:

```
hugo server
```

And you will get something like:

```
| EN
+------------------+----+
Pages            | 10
Paginator pages  |  0
Non-page files   |  0
Static files     |  3
Processed images |  0
Aliases          |  1
Sitemaps         |  1
Cleaned          |  0

Total in 11 ms
Watching for changes in /Users/bep/yourwebsitename/{content,data,layouts,static,themes}
Watching for config changes in /Users/bep/yourwebsitename/config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

Now, simply **navigate to your site in your browser at [http://localhost:1313/](http://localhost:1313/)**.

If you edit or create new files, you should see them updating live. If they don't, try force refresh your browser (cmd/ctrl + R).

## Build the Website

Once you're happy about your edits, it's time to actually build the website. It's *very* simple in Hugo. Simply run:

```
hugo
```

Hugo will now create all your HTML, CSS and JS assets needed for your website. The output will be in the `/public/` directory.

Congratulations, **you've built your own website!**

Now, if you're run your own web server, just copy the `/public/` directory to it to deploy your website.

If you don't, in the next section you will learn how to publish your new website for free and in an easy way, using GitHub and Netlify.

{{% tip %}}
Don't forget to tweak your configuration file before building and releasing your website to the public. In particular, you may want to update your base URL and website title accordingly.
```
baseURL = "https://example.org/"
languageCode = "en-us"
title = "My New Hugo Site"
theme = "hugo-tiu"
```
{{% /tip %}}
