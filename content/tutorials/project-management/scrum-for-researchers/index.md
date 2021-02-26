---
tutorialtitle: "Scrum for Researchers"
title: "Scrum for Researchers"
type: "scrum-for-researchers"
description: "Document and share data for internal and external use"
keywords: "scrum, project, sprint, team, management"
weight: 100
draft: false
author: "Pam Dupont"
authorlink: "https://www.tilburguniversity.edu/staff/p-h-dupont"
---

## How we learned to use Scrum

We, the very founders of Tilburg Science Hub, have used Scrum to manage the development of our project.

As time evolved, more people got involved in the process of developing Tilburg Science Hub and it became important to define roles, organize and coordinate working in a team efficiently, productively and pleasantly. By sharing our experiences with (a downsized version of) Scrum we hope to inspire and possibly help other teams to make their collaborations run smoothly.

However, we also advocate its adoption for any research project and whenever a team is involved. Keep reading to find out how to use it as a framework for collective research.

## Scrum in a nutshell

**[Scrum](https://www.scrum.org)** is a simple framework for effective team collaboration on complex products, co-created by Ken Schwaber and Jeff Sutherland.

Scrum defines three main roles: the product owner, Scrum master and development team members.

- The **product owner** is accountable for maximizing the value of the product and is also accountable for effective product backlog management, which includes:
    - Developing and explicitly communicating the Product Goal;
    - Creating and clearly communicating product backlog items;
    - Ordering product backlog items; and,
    - Ensuring that the product backlog is transparent, visible and understood.

- The **Scrum master** is accountable for the team’s effectiveness by coaching and helping the team members to focus, removing obstacles for the team and ensuring that tasks are completed in a positive, productive and timely manner.

- The **development team members** are responsible for completing the tasks in the Sprint.

During separately scheduled strategic discussions, the product owners (in collaboration with the team members) decide upon the needs for further development or improvement of the product. These needs form the **product backlog** and are broken down in smaller items/tasks that can be completed in a reasonable amount of time (for example a few hours). Items can be allocated to a specific team member.

For instance, during our team’s bi-weekly sprint planning meeting the product owners inspect the work from the backlog that’s most valuable to be done next and move these items to the sprint backlog.

The **sprint** is a period of (in our case) 2 weeks in which the team members complete the tasks selected by the product owners from the product backlog.

{{% tip %}}
To keep track of the product and sprint backlog and the items/tasks that’s being worked on, we suggest using **[Trello](https://trello.com)**, a tool by Atlassian to visualize and manage projects.
{{% /tip %}}

In addition to regular sprint meetings, every week we meet for a brief meeting (max 15 minutes) to discuss the past week’s "WOWs": basically, anything we have achieved and are very proud of sharing with the team. This helps us stay connected and positive!

{{% example %}}
**Scrum for a research project**

Think about the following situation. There are multiple co-authors who want to use publicly available data. They will analyze them with R. They have just come together to discuss how to proceed.

The goal is to program the whole workflow using [`make`](/building-blocks/configure-your-computer/automation-and-workflows/make/). The workflow consists of downloading the data, putting them in the right place, preparing them for analysis, producing summary statistics, and finally producing a pdf with those summary statistics.

The **starting point of the first meeting is creating a backlog** that consists of bite-size items that take a few hours (max) to complete.

So far, they have come up with the following items:
- Create directory structure;
- Create new Git repository;
- Write first raw version of code that downloads the data and saves them in the right place;
- Write first raw version of code that prepares the data for analysis;
- Write first simple analysis file that produces summary statistics and writes them into a LaTeX file;
- Set up a new tex file that produces a document with summary statistics table;
- Set up makefile so that make can be used to run the project.

Next, they have **the first sprint planning meeting** and discuss which items they want to **move to the sprint**. They are optimistic and move all of them to the next sprint. Importantly, particularly in times in which we have a lot of long online meetings, this is all they have to do, so the meeting can end.

During the sprint, **they all know what things need to be done**, so they can flexibly discuss with one another who does what. One can use Trello to **keep track** of this. Each entry above is a little card (think of it as a post-it note). Whenever someone starts working on something, the card is moved to the “in progress” section or column. And once something is finished, it ends up in the “done” column.

When people work very intensely on projects, they sometimes start the day with a brief meeting (a "stand-up" meeting) where the Scrum master manages the board and everyone coordinates who does what. In less intense times, one can instead have a weekly "WOW" meeting like we do.

In any case, after two weeks, the sprint ends with a review and after that, it’s time to look ahead. The **backlog has some new items** that the product owner has added, and the discussion is then again about which items should end up in the next sprint.
{{% /example %}}

## Why Scrum is useful and how to make it a success

We find Scrum helpful because it provides us with structure. That in turn leads to commitment and motivation. After all, it’s really satisfying to see many cards in the “done” column.

But Scrum is not the full answer. For instance, one needs to find a way to determine new items for the product backlog. This should not be done in the sprint planning meeting, because then one ends up having another long meeting every two weeks. Communication and discipline in the meetings are important.

In short, it can be seen as a structured way of working with meetings that are shorter and more productive, and cooperating in a flexible way in-between meetings.

## See also

- Learn more about Scrum [here](https://www.scrum.org)
- Read a more comprehensive [Scrum Guide](https://www.scrumguides.org/scrum-guide.html)
- Learn about how other researchers are using Scrum [here](http://crosstalk.cell.com/blog/scrum-for-science-a-framework-for-collective-research)
