---
title: "Principles for Good Coding"
description: "Make your code easy to understand for humans. If your code looks very complex or messy, you're probably doing it wrong."
keywords: "style, optimize, definition, human"
weight: 3
date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /write/good-code
---

## Write programs for people, not computers

Make your code easy to understand for humans. If your code looks very complex or messy, you're probably doing it wrong.

- Organization
    - Define functions that do one major step each, instead of one giant script doing everything
    - Write short scripts that do one task each
    - Document only what your code **doesn't** say, but nothing else
- Style
    - Use meaningful and short variable names
    - Use consistent code and formatting styles (oneExample, one_example, example-one)
    - Make use of indents in your code

## Define things once and only once

Let computers repeat and execute tasks.,

- Rule of 3: If you seem to copy-paste code 3 or more times, write a function instead and reuse that whenever you need that code.
- If you do something frequently, automate them so that the computer can do it for you instead. You can do this by:
    - using scripts, macros, aliases/variables
    - writing a dictionary with definitions
- Use build tools to [automate workflows](/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/automation/)

## Use a version control system

- Add all inputs, but no outputs/generated files
    - When you're saving your work, keep the things you created (inputs), but not the things the computer made from them (outputs/generated files; those will be [reproduced via a workflow](/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/automation/)). You can recreate outputs if needed.
    - Also [do not version large data inputs](/tutorials/project-setup/principles-of-project-setup-and-workflow-management/directories/).
- Work in small changes
    - Create [snapshots/commits](/building-blocks/share-your-results-and-project/use-github/versioning-using-git/) in small and logical steps. This way, you can understand how your project progressed and fix things if needed.
-  Use an issue tracking tool to document problems (e.g., such as the *Issue* tab on GitHub)

{{% warning %}}
Email is not an issue tracker!

{{% /warning %}}


## Optimize software only after it works correctly

Even experts find it hard to predict performance bottlenecks.

- Get it right, then make it fast
- Small changes can have a dramatic impact on performance
- Use a profile to report how much time is spent on each line of code

## Be a good code citizen
- Team members should take the time to improve the code they are modifying or extending even if they did not write it themselves.
- A core of good code plus a long series of edits and accretions equals bad code.
  - Why? The logical structure that made sense for the program when it was small no longer makes sense as it grows.

- It is critical to regularly look at the program as a whole and improve the logical structure through reorganization and abstraction. Programmers call this **refactoring**. Check this [link](https://refactoring.guru/refactoring/) to learn how to implement refactoring.

{{% tip %}}
- Even if your immediate task only requires modifying a small part of a program, we encourage you to take the time to improve the program more broadly.

- At a minimum, guarantee that the code quality of the program overall is at least as good as it was when you started.
{{% /tip %}}
## Keep it short
- No line of code should be more than 100 characters long.
  - All languages we work in allow you to break a logical line across multiple lines on the page (e.g, using `///` in Stata or `...` in Matlab).

{{% tip %}}
   Set your editor to show a “margin” at 100 characters.
{{% /tip %}}
- Functions should not typically be longer than 200 lines.

## Language-specific style guides
Want to learn language-specific coding guidelines? See the following building blocks for:

  - [Python](https://tilburgsciencehub.com/building-blocks/develop-your-research-skills/tips/python-coding-style/)
  - [R/R Studio](https://tilburgsciencehub.com/building-blocks/develop-your-research-skills/tips/r-code-style/)
  - [Stata](https://tilburgsciencehub.com/building-blocks/develop-your-research-skills/tips/stata-code-style/)


---
title: "R Coding Style Guidelines"
description: "Follow nice R coding style to make your code easier to understand and easier to the eye."
keywords: "style, code, R, guidelines, best practices"
weight: 5
date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /write/good-code/r
  - /r/style-guides
---
## Syntax

### Object names
- Variable and function names should only use letters, numbers, and underscores `(_)` and not include dots (mainly to avoid confusion with base R function names).  `CamelCases` are also fine.

 ```R
 #Good
 school_type
 SchoolType

 #Bad
 school.type
 ```
- Variable names should be as concise and meaningful as possible:

```R
#Good
day_one

#Bad
first_day_of_the_month
d1mth
```

### Spacing

Make code easier to read, place a space:

  - After a comma.

  ```R
  x[, 1]
  ```

  - After function arguments.

  ```R
  # Good
  function(x) {}

  # Bad
  function (x) {}
  function(x){}
  ```

  - Inside embracing operators `{ }`

  ```R
  group_by({{ by }}) %>%
  summarise(maximum = max({{ var }}, na.rm = TRUE))
  ```

  - Surrounding infix operators `(=, +, -, <-, etc.)`

  ```R
  mean(x, na.rm = TRUE)
  ```

### Function calls

- Omit names of data arguments, because they are used so frequently.
```R
# Good
mean(1:10, na.rm = TRUE)

# Bad
mean(x = 1:10, , FALSE)
mean(, TRUE, x = c(1:10, NA))
```

- Avoid assignment:

```R
# Good
x <- complicated_function()
if (nzchar(x) < 1) {
  # do something
}

# Bad
if (nzchar(x <- complicated_function()) < 1) {
  # do something
}
```
### Control flow

- Curly brackets `{ }` determine the hierarchy of your code. Make it clear.

  - `{` should be the last character on the line. Place in the line below (indented) the code to be run.

  - The contents should be indented by two spaces.

  - `}` should be the first character on the line. If it is the closing bracket, place it in a separate line with no indentation.

```R
if (y == 0) {
  if (x > 0) {
    log(x)
  } else {
    message("x is negative or zero")
  }
} else {
  y^x
}
```
{{% warning %}}
Note that, if an `if` statement is used, `else` should be on the same line as `}`. Moreover, if the statement is very simple, it might make more sense to just write it out all in one line.
```R
temperature <- if (x > 20) "nice" else "cold"
```
{{% /warning %}}


## Functions

### Naming functions
{{% tip %}}
  Try using verbs to name functions and nouns for variables.
{{% /tip %}}
```R
# Good
add_row()
permute()

# Bad
row_adder()
permutation()
```
### Explicit returns
Be clear about your intent to `return()` an object rather than relying on R's internal implicit return function.

```R
# Good
AddValues <- function(x, y) {
return(x + y)
}

# Bad
AddValues <- function(x, y) {
x + y
}
````
{{% tip %}}
  Avoid using `attach()` as it dramatically increases the chances of creating errors.
{{% /tip %}}

## Further material

In general, we follow [Google's R Style Guide](https://google.github.io/styleguide/Rguide.xml), which is based (and thus, so are we) on the [Tidyverse Style Guide](https://style.tidyverse.org/).

{{% warning %}}
**Exceptions to Google's R Style Guide:**

* We do not follow their naming conventions:
  * Do not use dots
  * Underscores or camel-case are fine.

* See [our conventions for line length](https://tilburgsciencehub.com/building-blocks/develop-your-research-skills/tips/principles-good-coding/)

* Not all functions need comment blocks explaining their purpose. However, it's encouraged to provide comments when a function's purpose might not be obvious or when the function will be used beyond the file where it's defined.

{{% /warning %}}
