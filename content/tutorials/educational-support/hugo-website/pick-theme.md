---
tutorialtitle: "Launch an Academic Website in 15 Minutes"
type: "hugo-website"
indexexclude: "true"
title: "Pick a Theme"
description: "Learn how to install a Hugo theme to make your website glossy."
keywords: "hugo, hugo-tiu, tilburg, static, website"
date: 2021-01-06T22:01:14+05:30
draft: false
weight: 12
author: "Andrea Antonacci"
authorlink: "https://www.tilburguniversity.edu/staff/a-d-antonacci"
aliases:
  - /get/hugo-tiu
  - /pick/hugo-theme
---

It's time you pick a theme for your website. This will determine how the content will look to the users. Head over to **[themes.gohugo.io](https://themes.gohugo.io)** and choose one!

We suggest [Academia Hugo](https://themes.gohugo.io/academia-hugo/) as a simple theme for personal websites, where you can showcase your portfolio, resume, and research work.

## Install a Theme

Each theme will have specific installation instructions. However, generally speaking, these are the required steps to set up a theme for your Hugo website:

1. You'll need to place the theme folder inside `yourwebsitename/themes`, usually by cloning the theme repository there.
2. You'll need to specify which theme you wish to use in the `config.toml`, `config.yaml`, or `config.json` file that is in the project's root directory.

{{% warning %}}
This second step may seem unnecessary, but it is there because Hugo allows you to "install" more than one theme - which basically means that you can have more than a theme folder inside `yourwebsitename/themes`. This is very useful if you want to quickly swap a theme and see how your website would look with a new one.

As a consequence, you need to explicitly tell Hugo (in the configuration file) which theme to use when building the site.
{{% /warning %}}

## Get Hugo-TiU

Meet `Hugo-TiU`, our new **Hugo open education theme for Tilburg University**, based on the original Hugo Book theme! The styling, fonts, and colors are inspired by the official Tilburg University website.

![Hugo-TiU](https://github.com/tilburgsciencehub/hugo-tiu/raw/master/images/screenshot.png)

{{% tip %}}
This theme is great for running open education classes. See, for instance, how Prof. Hannes Datta runs his [course on Online Data Collection and Management](https://odcm.hannesdatta.com) with `Hugo-TiU`.
{{% /tip %}}

We may be biased, but we love our new theme and we encourage you to use it!

{{% cta-primary "Learn more about Hugo-TiU" "https://github.com/tilburgsciencehub/hugo-tiu"%}}

### How to install Hugo-TiU

Installing `Hugo-TiU` is easy and similar to any other theme. However, being a custom-made theme, you won't find it on the official Hugo themes list at [themes.gohugo.io](https://themes.gohugo.io). Therefore, you can get it directly from its [GitHub repository](https://github.com/tilburgsciencehub/hugo-tiu):

1. Navigate to your Hugo project's root directory and run:

```
git submodule add https://github.com/tilburgsciencehub/hugo-tiu themes/hugo-tiu
```

2. Set ```theme = "hugo-tiu"``` or ```theme: hugo-tiu``` in your configuration file (in `config.toml` or `config.yaml`, respectively), either manually or from the command line:

{{% codeblock %}}
```toml
echo theme = "hugo-tiu" >> config.toml
```
```yaml
echo theme: hugo-tiu >> config.yaml
```
{{% /codeblock %}}

Alternatively, you can directly run Hugo and specify the theme as a flag:
```
hugo server --minify --theme hugo-tiu
```

That's it! In the next section, you will learn how to add some content to your website.

{{% summary %}}
**A brief recap**

Here's a very short example on how to create a new website **from scratch**:
```
hugo new site mydocs; cd mydocs
git init
git submodule add https://github.com/tilburgsciencehub/hugo-tiu themes/hugo-tiu
cp -R themes/hugo-tiu/exampleSite/content .
```
And then:
```
hugo server --minify --theme hugo-tiu
```
{{% /summary %}}
