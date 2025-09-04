---
type: "hugo-tutorial"
title: "(Part 4) Using Hugo: Add Content to Your Static Site"
description: "Learn how to add content to your Hugo site using Markdown and HTML"
draft: false
weight: 5
date: 2025-07-07
author: "Harold Miesen"
---

## (Part 4) Adding content to your site with Hugo using Markdown and HTML

Hugo uses [Markdown](https://www.markdownguide.org/) to write content. Markdown is a lightweight
markup language used to format plain text. It's simple to learn and allows you to add formatting
like bold, italic, links, lists, and more—all using plain text characters. Markdown is commonly
used for writing documentation, README files, and content for websites like GitHub, Reddit, and
Hugo because it's easy to write and read, even without special tools.

Markdown comes in different dialects—variations that extend the original syntax with features
like tables, footnotes, and syntax highlighting. Hugo uses __**Goldmark**__ as its default
Markdown parser, which is a modern implementation of the CommonMark specification. In addition
to the CommonMark core syntax, Goldmark supports several optional extensions—such as tables,
strikethrough, task lists, and typographic replacements—which can be enabled or disabled in
Hugo's configuration.

#### Headings

```
# H1
## H2
### H3
```

#### Emphasis

```
*italic* __**bold**__ `inline code`
```

#### Lists & Links

```
- Unordered item
1. Ordered item
&#91;Visit Hugo (URL)&#93;(https://gohugo.io)
```

#### HTML
Markdown supports raw HTML when you need more flexibility than Markdown syntax allows.

```
<pre>
  &lt;div class="custom-box"&gt;
  &lt;h3&gt;Hello from HTML!&lt;/h3&gt;
      &lt;p&gt;This content uses plain HTML inside a Markdown file.&lt;/p&gt;
  &lt;/div&gt;
</pre>
```

> Hugo will render this HTML as-is, even within `.md` files:

> <div class="custom-box">
>   <h3>Hello from HTML!</h3>
>   <p>This content uses plain HTML inside a Markdown file.</p>
> </div>

---

## Session 1: Adding an About Page to your Hugo Site
For the rest of this tutorial, we’ll assume you’ve launched a working Hugo site as described 
in the previous steps. We assume that:

- Hugo and the Ananke theme are installed correctly
- Your project structure looks something like this:

```
my-hugo-site/
├── config.toml
├── content/
├── layouts/
├── themes/
└── ...
```

### Step 1: Create a New Page
Use the Hugo CLI to create a new page called about.md:

```
hugo new about.md
```

Given that you have defined a default archetype (see the previous tutorial), this will create
a file at `content/about.md` with some default front matter:

```
---
title: "About"
date: 2025-07-16T10:00:00+01:00
draft: true
---
```

### Step 2: Add Your Content
Open `content/about.md` and add your content, for example:

```
---
title: "About"
date: 2025-07-16T10:00:00+01:00
draft: false
---

## Welcome to My Website

This is the About page. Here you can learn more about who I am and what this site is about.

- Built with Hugo  
- Theme: Ananke
```

> Make sure `draft: false` is set, so the page will be visible when building the site.

### Step 3: Add the Page to the Menu
Open your `config.toml` and add the page to the navigation menu:

```
[menu]
  [[menu.main]]
    identifier = "about"
    name = "About"
    url = "/about/"
    weight = 1
```

### Step 4: Preview the Site Locally
Start the Hugo development server in __**the root**__ of your project:

```
hugo server -D
```

Visit `http://localhost:1313` in your browser. You should now see an "About" link in the
top menu and the new page accessible.


## Session 2: Adding an Image to a Page in Hugo

### Step 1: Place the Image in Your Project
Images should go in the `static/` directory of your Hugo site. Files in this folder are
served directly at the root URL. For example, if you have an image called `profile.jpg`,
place it in "my-hugo-site/static/images/profile.jpg".

### Step 2: Reference the Image in Your Markdown File
Now edit your content file (e.g., `content/about.md`) and use standard Markdown to insert
the image: &#91;My Profile Picture&#93;(/images/profile.jpg).

This will render as an image with the alt-text “My Profile Picture”.

You can also use HTML if you need more control (e.g., setting width):
```
&lt;img src="/images/profile.jpg" alt="My Profile Picture" width="300"&gt;
```

### Step 3: Preview Locally
Run the server again in __**the root**__ of your project to preview the image:
```
hugo server -D
```
Go to `http://localhost:1313/about/` and check if the image appears.

> - All paths to images in `static/` are relative to the site root (e.g., `/images/...`).
> - The Ananke theme doesn’t style images by default, so you may want to add CSS later 
for alignment or sizing if needed.

## Session 3: Adding a Table in Markdown
Markdown supports simple tables, and they work well in Hugo—even with the Ananke theme.

### Step 1: Add a Table to Your Content File
Open a page like `content/about.md` and add the following Markdown:

{{%table%}}
| Project Title                    | Field              | Status       | Funding Source    |
|----------------------------------|--------------------|--------------|-------------------|
| Cognitive Mapping in AI          | Cognitive Science  | Active       | ERC Horizon 2020  |
| Climate Modeling with HPC        | Environmental Data | Completed    | National Science Fund |
| Quantum Information Theory       | Physics            | In Progress  | University Grant  |
{{/%table%}}

How it works:

- The first row defines the headers
- The second row of dashes (---) tells Markdown it’s a table
- Each | separates a column

__**Optional: Aligning Text in Columns**__
You can control alignment using colons:

{{%table%}}
| Left Aligned | Centered   | Right Aligned |
|:-------------|:----------:|--------------:|
| Text A       |   Text B   |        Text C |
| More A       |   More B   |        More C |
{{/%table%}}

- :-- = left aligned
- :--: = centered
- --: = right aligned

### Step 2: Preview Your Table
Run the Hugo server in __**the root**__ of your project:

```
hugo server -D
```

Then visit `http://localhost:1313` to see your table rendered in the browser.

- The Ananke theme doesn’t apply special styling to tables, but they are rendered correctly.
- You can customize the appearance later using CSS if needed.

## Session 4: Adding Custom CSS to Your Hugo Site

You can apply custom styles to your Hugo site by adding a CSS file manually and linking it in
your layout.

### Step 1: Create a CSS file
Create a file called `custom.css` in the `static/css/` directory:

```
your-hugo-site/
├── static/
│   └── css/
│       └── custom.css
```

Add some simple CSS, for example:

```
/* static/css/custom.css */
body {
  background-color: #f0f0f0;
  font-family: Arial, sans-serif;
}

h1 {
  color: #0066cc;
}
```

### Step 2: Link the CSS file in your HTML head
Edit the &lt;head&gt; section in your default layout file, usually at `layouts/_default/baseof.html`.

Add the following lines inside the `baseof.html` file. Your file might than look like:

```
<pre>
  &lt;!DOCTYPE html&gt;
  &lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title>{{ .Title }}&lt;/title&gt;
    &lt;link rel="stylesheet" href="/css/custom.css"&gt;
  &lt;/head&gt;
  &lt;body&gt;
    {{ block "main" . }}{{ end }}
  &lt;/body&gt;
  &lt;/html&gt;
</pre>
```

### Step 3: Run your site
Now start your Hugo site:

```
hugo server -D
```

> __**TIP**__: Since static/ maps directly to the root (/) in the output folder, placing your
CSS in `static/css/` makes it accessible at `/css/custom.css`.

Visit `http://localhost:1313` and you should see the styles applied.

You're now ready to build and publish static sites with Hugo, and add content to it!
Go back to
[Hugo Tutorial: Start Here](../1-index/).

## Resources
- [Hugo Docs](https://gohugo.io/documentation/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Ananke Theme](https://github.com/theNewDynamic/gohugo-theme-ananke)
