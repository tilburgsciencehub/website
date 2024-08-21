---
title: "R Coding Style Guidelines"
description: "Follow nice R coding style to make your code easier to understand and easier to the eye."
keywords: "style, code, R, guidelines, best practices"
weight: 3
date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /write/good-code/r
  - /r/style-guides
---

## Overview

Writing clean, and consistent code is crucial for effective collaboration and reproducibility. Following a standardized coding style not only makes your code easier to understand but also helps avoid errors. This guide outlines key best practices for R coding style and is divided into two sections: *Syntax* and *Functions*. 

{{% tip %}}

Familiarize yourself with the basics before diving into coding style:

- [Set up R/RStudio](/topics/computer-setup/software-installation/rstudio/r/)
- [Getting started with R](/topics/computer-setup/software-installation/rstudio/getting-started-with-r-overview/)

{{% /tip %}}



## Syntax

Syntax refers to the foundational rules that determine how your code should be written and structured. Following good syntax helps ensure that your code is not only function but also readable and maintainable. 

### Object names

- Variable and function names should consist only of letters, numbers, and underscores `(_)`. Avoid using dots in names to avoid confusion with base R function names. Both `snake_case` and `CamelCase` are also fine.

{{% codeblock %}}
 ```R
 #Good
 school_type
 SchoolType

 #Bad
 school.type
 ```
{{% /codeblock %}}
 
- Variable names should be as concise and meaningful as possible:

{{% codeblock %}}
```R
#Good
day_one

#Bad
first_day_of_the_month
d1mth
```
{{% /codeblock %}}


### Spacing

Make code easier to read, place a space:

- After commas:

{{% codeblock %}}
```R
  x[, 1]
```
{{% /codeblock %}}

- After function arguments:

{{% codeblock %}}

```R
# Good
function(x) {}

# Bad
function (x) {}
function(x){}
```
{{% /codeblock %}}

- Inside curly braces `{ }` when using them to embrace operators:

{{% codeblock %}}
```R
group_by({{ by }}) %>%
summarise(maximum = max({{ var }}, na.rm = TRUE))
```
{{% /codeblock %}}


- Surround infix operators `(=, +, -, <-, etc.)` with spaces:

{{% codeblock %}}
```R
mean(x, na.rm = TRUE)
```
{{% /codeblock %}}


### Function calls

- Omit argument names for frequently used data arguments unless it adds clarity. 

{{% codeblock %}}
```R
# Good
mean(1:10, na.rm = TRUE)

# Bad
mean(x = 1:10, , FALSE)
mean(, TRUE, x = c(1:10, NA))
```
{{% /codeblock %}}


- Avoid complex assignments within control flow statements:

{{% codeblock %}}
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
{{% /codeblock %}}

### Control flow

Curly brackets `{ }` define the hierarchy of your code, so it's important to use them clearly. 

  - Place `{` on the same line as the opening statement, as the last character.
  - The code inside the brackets should be placed on the next line and indented by two spaces.
  - The `}` should be the first character on the line. If it is the closing bracket, it should appear on its own line, without indentation.

{{% codeblock %}}
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
{{% /codeblock %}}

{{% tip %}}

*If-else statements*

- When using an `if` statement, the `else` should be placed on the same line as the closing `}` of the `if` block. 

```R
if (x > 0) {
  print("Positive number")
} else {
  print("Non-positive number")
}
```

- If the statement is straightforward, you can simplify the code by writing the entire statement on one line.

```R
temperature <- if (x > 20) "nice" else "cold"
```

{{% /tip %}}


## Functions

Functions are fundamental for encapsulating and reusing code, allowing you to structure your project more efficiently.


### Naming functions

Functions should have descriptive names that indicate their actions. Try using verbs for function names. For variables, that represent data or state, nouns are more appropriate.

{{% codeblock %}}

```R
# Good
add_row()
permute()

# Bad
row_adder()
permutation()
```
{{% /codeblock %}}


### Explicit returns

Be explicit when returning values from functions. While R implicitly returns the last evaluated expression, using `return()` improves clarity, especially in complex functions.

{{% codeblock %}}
```R
# Good
AddValues <- function(x, y) {
return(x + y)
}

# Bad
AddValues <- function(x, y) {
x + y
}
```
{{% /codeblock %}}


{{% tip %}}
Avoid using `attach()` as it increases the likelihood of creating errors dramatically, due to unintended variable masking or overwriting the workspace.
{{% /tip %}}

## Further reading

In general, this guide follows the [Google's R Style Guide](https://google.github.io/styleguide/Rguide.xml), which is based (and thus, so are we) on the [Tidyverse Style Guide](https://style.tidyverse.org/). We align with those guides but have *a few exceptions* worth noting.

* We do not follow their naming conventions:
  * Do not use dots
  * Underscores or CamelCase are fine.

* Our conventions for line length differ. See [our principles for good coding](/topics/computer-setup/develop-coding-skills/coding-practices/principles-good-coding/) for more details.

* We do not require that all functions have a comment block describing their uses. We encourage you to do so when the purpose of a function is not clear or whenever the function is used outside of the file in which it is defined.

{{% summary %}}

Whether you are working solo or within a team, these best practices ensure that your R code is efficient and easy to understand. 

{{% /summary %}}
