---
title: "R coding style guidelines"
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
- Variable and function names should use only letters, numbers, and underscores `(_)` and not include dots (mainly to avoid confusion with base R function names).  `CamelCases` are also fine.

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

  - `{` should be the last character on the line. Place in the line below (indented) the code to be ran.

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
  Try using verbs to name functions. Instead, try using nouns for variables.
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
Be clear about your intent to `return()` an object instead of relying on R's internal implicit return function.

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
  Avoid using `attach()` as it increases dramatically the chances of creating errors.
{{% /tip %}}

## Further material

In general, we follow [Google's R Style Guide](https://google.github.io/styleguide/Rguide.xml), which is based (and thus, so are we) on the [Tidyverse Style Guide](https://style.tidyverse.org/).

{{% warning %}}
**Exceptions to Google's R Style Guide:**

* We do not follow their naming conventions:
  * Do not use dots
  * Underscores or camel-case are fine.

* See [our conventions for line length](https://tilburgsciencehub.com/building-blocks/develop-your-research-skills/tips/principles-good-coding/)

* We do not require that all functions have a comment block describing their uses. We encourage to do so when the purpose of a function would not be clear or whenever the function will be used outside of the file in which it is defined.

{{% /warning %}}
