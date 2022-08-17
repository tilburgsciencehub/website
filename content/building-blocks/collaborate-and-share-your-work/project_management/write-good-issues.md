---
title: "Write GitHub Issues That Get the Job Done"
description: "You'll learn how to write good GitHub issues that get the job done. See our issue templates and learn the best practices for good GitHub issue management"
keywords: "issues, project, git, github, issue, best practices, template, issue management"
weight: 3
#date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /write/issues
  - /use/issues
  - /building-blocks/collaborate-and-share-your-work/use-github/write-good-issues/
---

## Overview

### Why Issues?

[Github Issues](https://guides.github.com/features/issues/) can be used to clearly define tasks that either you or your team members will eventually work on. In combination with Kanban-style GitHub Project boards, they become a compelling way of coordinating teamwork. They also help you keep track of what's happening on projects and provide a durable, replicable record of the work for future reference.

### Getting Started with Issues

1. Every issue has a __creator__ (i.e., the person who created it) and should have __one or more assignees__ (the person(s) who will execute it). The creator chooses the assignee when the issue is created.
2. An issue is a __discrete, well-defined unit of work on a project__. Usually, this means that an issue should not be more than a couple of weeks' worth of work and should not be open for more than a month or two.
3. Issues are __adaptive__. For example, an issue that started with manageable scope may grow as the project expands or new questions arise. At this point, carve off subparts into separate issues and close the original issue with an interim summary.
4. Issues are prioritized using the __Project Board on GitHub__. If you have time left, you can work on open issues that are not yet part of your current sprint.

All such rules are just a guideline. Using your time productively takes precedent over the priority ordering of tasks.


{{% warning %}}
One common problem with Issues is that they are formulated too broadly. They then are likely to become open-ended and end up mixing multiple work threads.

"Write the follow-up paper" or "Do the analysis" are usually not good issues (unless the project is tiny).

{{% /warning %}}


<!--
Issues should not be opened until the assignee is ready to work on them actively (or will be soon). To-do items that we plan to work on in the future should be placed on a project outline in the repository's Github wiki.
-->

<!--
If work stops on an issue for any reason and is not expected to resume soon, the issue should be closed with an interim summary. If we plan to continue work later, this can be noted on the project outline in the repository's Github wiki, along with a link to the original issue.
-->

## Best Practices for Writing GitHub Issues

### Use Descriptive Titles!

- The issue title should be descriptive enough that somebody looking back at it later will understand what the purpose of the issue was and how it fits into the larger context.
- Titles should use the *imperative mood*, and not end in a period ("Revise the main figure") not ("main figure.").
- [This post](https://chris.beams.io/posts/git-commit/) by Chris Beams has an excellent discussion of what makes a good Git commit message; the same principles apply to good issue titles as well.

{{% tip %}}

__Good issue titles__

* Revise abstract
* Add new data to main robustness figure
* Run bootstrap for IV regressions

__Bad issue titles__

* abstract
* Robustness
* Incorrect inputs causing error.

Note that you can also *change* the title of an issue to make it more accurately reflect the current task.

{{% / tip %}}

### Set Goals with Clear Descriptions

- State the __goals of the issue clearly__.
- Be __explicit about the deliverables__.
- Like the title, it should usually be written in __imperative mode__.
- The description should be __precise enough that a third party can judge__ whether the issue was completed or not.
- It should include enough __explanation and context__ that someone who is not intimately familiar with the other work going on at that moment can understand it clearly -- remember that we will often be returning to these issues many months or even years later and trying to understand what was going on.
- If an issue __relates directly to one or more other issues__, this should be stated in the description with a link to the other isssue(s) (e.g., "Follow-up to #5").

<!--The same principles regarding hyperlinks, @-references, etc. in the discussion of [comments](https://github.com/tilburgsciencehub/onboard/wiki/Issues#comments) below apply to issue descriptions as well.
-->

{{% tip %}}

__Good description__

*Following #22, re-run the analysis on Research Cloud to see if that improves performance.*
* *Run a minimal version of the base model on VM1*
* *Test the subsampling procedure on VM1*
* *Run a minimal version of the base model on VM2*
* *Test the subsampling procedure on VM2*

*Document necessary code changes to implement our updated code and potential bottlenecks.
In the long term, we want to migrate all of our model computations to Research Cloud.*

__Bad description__

*Redoing everything on Research Cloud, including the subsampling. Remember we want to test VM1, not only VM2.*

{{% / tip %}}

### Comments Document Your Progress

Comments in Github Issue threads are the main way we communicate about our work.

- You can add comments to the thread in a browser or by replying to a notification email about the issue. When commenting by email reply, remember to *delete the quoted text of the email thread below your actual reply*. Otherwise, this will add duplicate text to the comment thread and make it hard to read.
- You (the assignee) should post comments regularly summarizing progress.
  - The comment threads are your real estate, and you are free to include updates as often as you find helpful.
  - Preliminary output, "notes to self," etc., are acceptable.
  - No issue should be left for more than two weeks without a comment updating the status, even if the comment only says: "Have not done any work on this issue in the last week."
- If you have a question that requires input or attention from another lab member, you should write a comment, including an '@' reference, that clarifies precisely what information is needed.
  - For example, `@hannesdatta, Where would you like me to store the data files?`
  - Users should keep email notifications for `@` references turned on. Anyone who is not the assignee of an issue will assume by default that comments not @-referencing them do not require their attention.

- It is up to you to judge the optimal time to request feedback from the reporter (or PIs on the project, etc.). You should usually not send results until you have made sure they are correct and make sense. When you request feedback, you should provide a clear and concise summary, making the situation clear and exactly what input you need. At the same time, you should not feel shy about requesting feedback when you are confident it will be efficient and valuable.

- If you have an important interaction about an issue outside of GitHub -- in person, over video chat, etc. -- add a comment to briefly summarize the content of that interaction and the conclusions reached.

- Issues are referenced by their Github issue number (e.g., "#5") when it is clear from the context what repository the issue is in, or by the name of the repository plus the issue number (e.g., "news_trends #5") when it is not. Any reference to a Github issue in a comment thread, email, etc., should be hyperlinked to the issue itself. Note that Github does this automatically if you type "#" followed by a number in a Github issue thread.

- Any reference to a file, directory, paper, or webpage should be hyperlinked to a permanent URL. [This page](https://help.github.com/articles/getting-permanent-links-to-files/) has instructions for getting permanent URLs for files in Github repositories. Links to Dropbox files and directories can be copied from the web or desktop client.



### Provide Deliverables

__Every issue must conclude with a reproducible deliverable.__

* It is up to you (the assignee) to judge when the objectives in the task description plus any issues that have come up in the comment stream have been resolved. As a rule, you do not need to request confirmation from the issue’s creator (or project lead).

* Each task should have a final deliverable containing all relevant results. The form of the deliverable may be any combination of:
  - Content at Tilburg Science Hub
  - Content added to a research project (e.g., a draft of a paper, slides, analysis) in the project repository
  - A PDF or markdown file
  - A summary in the final comment in the issue thread

* The deliverable must be __self-contained__. It should usually begin with a concise summary of the task goal and the conclusions (e.g., answer to an empirical question), followed by supporting detail. A user should learn all relevant results from the deliverable without looking back at the comment thread or task description.

{{% tip %}}
__Use this template to start writing issues__

```
# Goal of this issue

Clearly define the goal.

# Resources

Say which resources to use (e.g., where to find relevant code, papers, etc.).

# Deliverables

Clearly define deliverables. Mention deadlines if necessary.
```

{{% /tip %}}

<!--

By default, we produce PDF/markdown deliverables inside the repository, following the same rules to produce papers, slides, etc. Code and documents specific to the issue and that we will not want to carry forward in the repository after the issue is complete can be created in the issue [branch](https://github.com/tilburgsciencehub/onboard/wiki/Workflow#branch) and then deleted before merging back to master. Such files are usually placed in a separate subdirectory called `/issue/` at the top level of the repository. [Permanent links](https://help.github.com/articles/getting-permanent-links-to-files/) to deliverables in the `/issue/` subdirectory will continue to work even after the directory is deleted.


The deliverable must contain enough information that another user could replicate its results. For figures, tables, or other results produced by code, a user should identify the relevant code and reproduce the output. This will usually be automatic when the output is produced inside the repository. For output produced by hand (e.g., literature reviews, manual calculations), the deliverable should include enough information about the steps performed that a user could have a decent shot at repeating them.

-->


### Closing Issues

* When an issue is complete, you should post a final summary comment and then close it.
* All closed issues must have one and only one summary comment. 
* If changes made after the issue is closed (e.g., during peer review) require changes, you should edit the summary comment in place rather than creating a new one.
* At this point, you will also normally open a [pull request](https://github.com/tilburgsciencehub/onboard/wiki/Workflow#pull-request) to peer review the issue and merge the issue branch back to master.

{{% tip %}}
__Close an Issue with a final comment__

* Your final comment should begin with "Summary" on the first line (usually bold or title font).
* It must also include a brief (usually a couple of paragraphs) recap of what was accomplished in the issue.
* It must include a [revision-stable](https://help.github.com/en/github/managing-files-in-a-repository/getting-permanent-links-to-files) pointer to the deliverable -- usually a link along with additional information if needed (e.g., relevant page/table/figure numbers in the draft), or reference to a branch on GitHub.

{{% /tip %}}

### Setting Priorities

- Priorities to work on issues are coordinated using the Project Boards on GitHub.
- If you have time left in your sprint, you can work on other open issues.
- In prioritizing your work, note that peer review takes priority over all open issues; open issues created earlier should take precedence over tasks created later.
- In some cases, we may give explicit instructions that override these defaults (e.g., we tag an issue with "good issue to start", or "critical"). If you are ever unsure about prioritization, you should ask.
