---
tutorialtitle: "Scrum for Researchers"
title: "Scrum for Researchers"
type: "scrum-for-researchers"
description: "Discover Scrum to improve your project management when working on empirical research projects"
keywords: "scrum, project, sprint, team, management"
weight: 100
draft: false
author: "Pam Dupont"
authorlink: "https://www.tilburguniversity.edu/staff/p-h-dupont"
aliases:
  - /learn/scrum
---

## How we learned to use Scrum

We use [Scrum](https://www.scrum.org) - a simple framework for effective team collaboration - to manage the development of Tilburg Science Hub. By sharing our experiences with (an admittedly customized version of) Scrum, we hope to inspire and possibly help other teams to make their collaborations run smoothly.

Importantly, Scrum works for any type of project, including __academic research projects__.
Keep on reading to find out how to use Scrum as a framework for collective research!

## Scrum in a nutshell

### Team members have different roles

Scrum defines three main roles for members of the team: the product owner, the Scrum master and development team members.

- The **product owner** is accountable for maximizing the value of the product and for defining a clear "task list" (called product backlog), including:
    - Developing and explicitly communicating the Product Goal;
    - Creating and clearly communicating product backlog items;
    - Ordering product backlog items; and,
    - Ensuring that the product backlog is transparent, visible and understood.

- The **Scrum master** is accountable for the team’s effectiveness by coaching and helping the team members to focus, removing obstacles for the team and ensuring that tasks are completed in a positive, productive and timely manner.

- The **development team members** are responsible for completing the tasks in the Sprint.

### Meeting types and planning

- During separately scheduled __strategic discussions__, the product owners (in collaboration with the team members) decide upon the needs for further development or improvement of the product. These needs form the *product backlog* and are broken down in smaller items/tasks that can be completed in a reasonable amount of time (for example a few hours). Items can be allocated to a specific team member.

- During our team’s __sprint planning meeting__, which kicks off each new sprint, the product owners inspect the work from the backlog that’s most valuable to be done next and move these items to the sprint backlog. We also review tasks that have been completed in the previous sprint.

- __During the sprint__ (in our case a two-week period), team members complete the tasks selected by the product owners from the product backlog.

- In addition to regular sprint meetings, every week we meet for a brief __"WOW meeting"__ (max. 15 minutes) to discuss the past week’s successes: basically, anything we have achieved and are very proud of sharing with the team. This helps us stay connected and positive!

{{% tip %}}

To get started with using Scrum...
- determine the roles of team members,
- pick a sprint duration (e.g., two weeks),
- plan a strategic discussion so that you converge on the backlog items,
- schedule your first sprint planning meeting,
- schedule the "weekly wows", and
- reserve time in your agenda to work on tasks assigned to you.

To keep track of the product and sprint backlog and the items/tasks that’s being worked on, you can use **[Trello](https://trello.com)** or the project tab on your project's [GitHub repository](https://github.com). Start by creating these "tabs"/columns now:
- backlog,
- sprint (to do),
- sprint (in progress),
- sprint (done), and
- notes to keep (in which to pin important links so you don't lose them).

{{% /tip %}}


{{% example %}}
**Using Scrum for a research project**

Think about the following situation. There are multiple co-authors who want to use publicly available data. They will analyze them with R. They have just come together to discuss how to proceed.

The goal is to develop a workflow using [`make`](/building-blocks/configure-your-computer/automation-and-workflows/make/). The workflow consists of downloading the data, putting them in the right place, preparing them for analysis, producing summary statistics, and finally producing a PDF with those summary statistics.

The **starting point of the first meeting is creating a backlog** that consists of bite-size items that take (max.) a few hours to complete.

So far, the team members have come up with the following items:
- Create directory structure,
- Create new Git repository,
- Write first raw version of code that downloads the data and saves them in the right place,
- Write first raw version of code that prepares the data for analysis;
- Write first simple analysis file that produces summary statistics and writes them into a LaTeX file;
- Set up a new tex file that produces a document with summary statistics table;
- Set up makefile so that make can be used to run the project.

Next, the team members have **the first sprint planning meeting** and discuss which items they want to **move to the sprint**. They are optimistic and move all of them to the next sprint. Importantly, particularly in times in which we have a lot of long online meetings, this is all they have to do, so the meeting can end.

During the sprint, **they all know what things need to be done**, so they can flexibly discuss with one another who does what. One can use Trello or the project board on GitHub to **keep track** of this. Each entry above is a little card (think of it as a post-it note). Whenever someone starts working on something, the card is moved to the “in progress” section or column. And once something is finished, it ends up in the “done” column.

When people work very intensely on projects, they sometimes start the day with a brief meeting (a "stand-up" meeting) where the Scrum master manages the board and everyone coordinates who does what. In less intense times, one can instead have a weekly "WOW" meeting like we do.

In any case, after two weeks, the sprint ends with a review and after that, it’s time to look ahead. The **backlog has some new items** that the product owner has added, and the discussion is then again about which items should end up in the next sprint.
{{% /example %}}

## Why Scrum is useful and how to make it a success

We find Scrum helpful because it provides us with structure. That in turn leads to commitment and motivation. After all, it’s really satisfying to see many cards in the “done” column.

But Scrum is not the full answer. For instance, one needs to find a way to determine new items for the product backlog. This should not be done in the sprint planning meeting, because then one ends up having another long meeting every two weeks. Communication and discipline in the meetings are important.

In short, Scrum can be seen as a structured way of working with meetings that are shorter and more productive, and cooperating in a flexible way in-between meetings.

## See also

- Learn more about Scrum [here](https://www.scrum.org)
- Read a more comprehensive [Scrum Guide](https://www.scrumguides.org/scrum-guide.html)
- Learn about how other researchers are using Scrum [here](http://crosstalk.cell.com/blog/scrum-for-science-a-framework-for-collective-research)
