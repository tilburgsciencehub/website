---
tutorialtitle: "Create Your Own Website in 15 Minutes"
type: "hugo-website"
title: "Hugo Website Overview"
description: "Learn how you can launch your very own static website in a quick and easy way."
keywords: "hugo, static, website, generator, class, academic"
weight: 10
date: 2020-11-11T22:01:14+05:30
draft: false
author: "Andrea Antonacci"
authorlink: "https://www.tilburguniversity.edu/staff/a-d-antonacci"
aliases:
  - /launch/academic-website
  - /launch/hugo-website
  - /create/personal-website
  - /tutorials/open-education/hugo-website/hugo-website-overview/
  - /tutorials/code-like-a-pro/hugo-website/_index
  - /tutorials/educational-support/hugo-website/overview/
  - /tutorials/open-education/hugo-website/overview/
---

## Why to Launch a Website?

Whether you want to spread the word about your research work or to share content with your students in open education classes, getting your very own website to do so would help you immensely.

A few ideas of what you could do with a personal website:

- Showcase your own academic profile and research work in a professional way
- Disclose data and share your results with the world
- Run your open education classes, publishing the syllabus, lectures, exercises...
- Maintain a collection of articles or blog posts
- Virtually anything else!

However, getting a new website up and running is often perceived as a daunting and expensive task, especially if you're not really an IT guy. No worries! In this tutorial, you will learn how to launch a static website within minutes, **free of charge**, and without writing a single line of code.

## The Basics

### First off, what is a static website?

A **static website** serves exactly the same content to all users (with just a few exceptions). All the web pages delivered to the users are also exactly as stored - think of Wikipedia.

By contrast, **dynamic websites** show different content depending on the user accessing them. For instance, your Facebook newsfeed would probably look a bit different from Barack Obama's one.

As you may have guessed, in this guide we will deal only with static websites because they are easier and cheaper to set up and maintain, they're faster, safer and work great for our purposes.

### Enter the World of Static Site Generators

Static Site Generators (SSGs) combine content with templates to generate the pages of a website. For instance, you can write your content in Markdown and then pick a template to choose how the content will be displayed.

In other words, SSGs are not too rigid on how the frontend of your site is built: once you write the content, you're free to change "how it looks" as many times as you want. It's up to the SSG to generate the HTML, CSS and JS assets accordingly.

There are [many SSGs out there](https://jamstack.org/generators/) in just about any programming language. We encourage you to spend some time researching which one works best for you if you're serious about this.

{{% tip %}}
Don't overestimate the importance of which programming language the SSG is based on. You don't need to know that language, unless you require some custom modifications.
{{% /tip %}}

### Hugo

For the purposes of this tutorial, we choose **[Hugo](https://gohugo.io)**, a very popular SSG written in Go, which is *very* fast. You will learn how to use it in the next sections.
