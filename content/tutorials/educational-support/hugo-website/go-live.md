---
tutorialtitle: "Create Your Own Website in 15 Minutes"
type: "hugo-website"
indexexclude: "true"
title: "Go Live!"
description: "Learn how to publish your static website with GitHub and Netlify."
keywords: "hugo, netlify, domain, dns, github"
date: 2021-01-06T22:01:14+05:30
draft: false
weight: 14
author: "Andrea Antonacci"
authorlink: "https://www.tilburguniversity.edu/staff/a-d-antonacci"
aliases:
  - /publish/website
  - /setup/netlify
---

## How to Host Your Website

Because your website is static, it can be hosted virtually anywhere using any web server.

However, we highly suggest you to deploy your website using **[Netlify](https://www.netlify.com)**.

Netlify can host your website for free, it's very easy to use since it's linked to your GitHub profile, and it provides some great perks, like a global CDN, free SSL certificates and continuous deployment.

## The Last Piece of the Puzzle

1. First, if you haven't done it already, create a new GitHub repository for your website. If you don't know how, you can read about it [here](/learn/versioning).

2. Add and commit a new file to your repo, called `netlify.toml`. This file is a sort of recipe for Netlify on how to build your website. Inside the file, write the following:

{{% codeblock %}}
```toml
[build]
  command = "hugo --gc --minify -b $URL"
  publish = "public"

[build.environment]
  HUGO_VERSION = "0.81.0"
  HUGO_ENABLEGITINFO = "true"

[context.production.environment]
  HUGO_ENV = "production"

[context.deploy-preview]
  command = "hugo --gc --minify --buildFuture -b $DEPLOY_PRIME_URL"

[context.branch-deploy]
  command = "hugo --gc --minify -b $DEPLOY_PRIME_URL"
```
{{% /codeblock %}}

3. Create a new Netlify account. Go to [app.netlify.com](https://app.netlify.com/) and **sign up using GitHub**. Select "Authorize application" when prompted.

4. Now create a "**New site from Git**".

![New site from Git](https://d33wubrfki0l68.cloudfront.net/1a92de85be074abc024967fa7088c8b719c32466/f7496/images/hosting-and-deployment/hosting-on-netlify/netlify-add-new-site.jpg)

5. Follow the required steps. You will need to select and authorize GitHub again (this time with added permissions to your repos).

6. Select your new website repository. You can then change a few setup options.
    - Keep publishing from the `master` branch
    - The build command is: `hugo` (or the specified command in the `netlify.toml`)
    - The default publish directory is `public`

7. Deploy!

![Deploy with Netlify](https://d33wubrfki0l68.cloudfront.net/a9f55d92792a554cb775cd0d10eddf445338b83a/0a424/images/hosting-and-deployment/hosting-on-netlify/netlify-deploying-site.gif)

8. Once it's done, you should see a successful message and an URL for your website (which has been automatically generated for you). You can change the URL in "Settings". You can now **visit your live website!**

![Netlify successful message](https://d33wubrfki0l68.cloudfront.net/e2ea775b0985b93f2e0d7c88ae134e90c3e7446e/8a3d7/images/hosting-and-deployment/hosting-on-netlify/netlify-deploy-published.jpg)

{{% warning %}}
**You've made it!**

You created a website with continuous deployment. What does that mean?

It means that Netlify is now actively "watching" your GitHub repository.

**Every time you commit to your repository, the website will be automatically rebuilt and redeployed!** You no longer need to deal with Netlify. From now on, you can edit your website locally, and when you're happy about the edits, you can **simply commit**. Pretty neat, isn't it?
{{% /warning %}}

## See Also

- Learn how to [add a custom domain](https://docs.netlify.com/domains-https/custom-domains/) to your Netlify-hosted website
- Learn how to [set up HTTPS on custom domains](https://docs.netlify.com/domains-https/https-ssl/)
- Check out [other hosting and deployment options](https://gohugo.io/hosting-and-deployment/)
- Read a more [detailed guide](https://gohugo.io/hosting-and-deployment/hosting-on-netlify/) on how to host your Hugo website on Netlify
