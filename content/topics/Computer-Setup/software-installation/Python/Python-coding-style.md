---
title: "Python Coding Style Guidelines"
description: "Follow nice language-specific coding styles to make your code easier to understand and easier to the eye."
keywords: "style, code, python, best practices, guidelines"
weight: 2
date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /write/good-code/python
  - /python/style-guides
---

# Overview

We follow the Python's style guide, [PEP 8](https://www.python.org/dev/peps/pep-0008/#programming-recommendations), emphasizing readability and consistency. In this topic, we highlight some of the best practices with code examples. 

Note that sometimes your judgment is required, decide what looks best even though it doesn't always comply with the guidelines!

## Straightforward code

Keep the code as explicit and readable as possible. Both examples below return the same thing, while with the good example it is more obvious what is happening.

{{% codeblock %}}
```python

# Good
def make_complex(x, y):
    return {'x': x, 'y': y}

# Bad: complexer than necessary
def make_complex(*args):
    x, y = args
    return dict(**locals())
```
{{% /codeblock %}}

## Naming conventions

Use concise and meaningful names for variables, functions, classes, and modules. Avoid using dots (.) in names to prevent confusion with Python attributes and methods.

- Function: function, my_function
- Variable: x, var, var2, my_variable
- Class: Model, MClass
- Method: class_method, method
- Constant: CONSTANT, MY_CONSTANT
- Module: module.py, my_module.py
- Package: package, mypackage

{{% codeblock %}}
```python
# Good
school_type
SchoolType

# Bad
school.type
```
{{% /codeblock %}}

## Maximum line length and line breaking

PEP 8 suggests lines should be limited to 79 characters. Python will assume line continuation if code is contained within parentheses, brackets, or braces:

{{% codeblock %}}
```python

# Good
def long_function_name(
      var_one, var_two, var_three,
      var_four, var_five, var_six):
    print(var_one)

# Bad
def long_function_name(var_one, var_two, var_three,var_four, var_five, var_six):
    print(var_one)
```
{{% /codeblock %}}

It is good practice to put the operators on the beginning of a new line, rather than breaking the line after the operator.

{{% codeblock %}}
```python
# Good
sum = (var1 
      + var2
      - var3)

# Bad
sum = (var1 + 
       var2 -
       var3)
```
{{% /codeblock %}}

## Indentation and continuation lines

- Use 4 spaces per indentation level
- Align wrapped elements vertically within parentheses, brackets, and braces.
- Avoid arguments on the first line without vertical alignment 

{{% codeblock %}}
```python
# Good
fun = long_function_name(
    var_one, var_two
    var_three, var_four)

# Bad: arguments on first line
foo = long_function_name(var_one, var_two,
    var_three, var_four)
```
{{% /codeblock %}}

Closing symbols may align with the first non-whitespace character of the last line or the first character of the line starting the construct.

{{% codeblock %}}
```python

# Both options work.
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]

my_list = [
    1, 2, 3,
    4, 5, 6,
]
```
{{% /codeblock %}}

## Imports
- Place imports on separate lines for clarity and readability.
- Organize imports in the following groups with blank lines between them: standard library imports, related third-party imports, local application/library-specific imports.
- Always place imports at the top of the file before other code.

{{% codeblock %}}
```python
# Good
import os
import sys

# Bad
import sys, os
```
{{% /codeblock %}}

## Whitespace

Avoid extraneous whitespace
- Immediately inside parentheses, brackets, or braces

{{% codeblock %}}
```python
# Good
buy(item_list[0], {inventory: 2})

# Bad
buy( item_list[ 0 ], { inventory: 2 } )
```
{{% /codeblock %}}

- Before a comma, semicolon, or colon

{{% codeblock %}}
```python
# Good
if x == 2: print(x, y); x, y = y, x

# Bad
if x == 2 : print(x , y) ; x , y = y , x
```
{{% /codeblock %}}


- Before the open parenthesis that starts the argument list of function call

{{% codeblock %}}
```python
# Good
buy(1)

# Bad
buy(1)
```
{{% /codeblock %}}

- Between a trailing comma and a closing parenthesis

{{% codeblock %}}
```python
# Good
foo = (0,)

# Bad
foo = (0, )
```
{{% /codeblock %}}

- To align assignment operators

{{% codeblock %}}
```python
# Good
x = 1
y = 2
long_variable = 3

# Bad
x             = 1
y             = 2
long_variable = 3
```
{{% /codeblock %}}


- At the end of a line (known as trailing whitespace). It is usually invisible, but can be confusing. 

## Comments

- Use docstrings for functions whose purpose may be unclear or that will be used outside of their own modules. 
- Limit the line length of comments and docstrings to 72 characters.
- Use complete sentences, starting with a capital letter.
- Use inline comments sparingly.
- Write inline comments on the same line as the statement they refer to.
- Separate inline comments by two or more spaces from the statement, and start them with a # and a single space.

{{% codeblock %}}
```python

"""This is a docstring""".

x = 123  # This is an inline comment.
```
{{% /codeblock %}}

## Boolean value comparison

Avoid comparing boolean values to `True` or `False` using `==`, instead use if statements.

{{% codeblock %}}
```python
# Good
if attr:
    print('attr is truthy!')

# Bad
if attr == True:
  print('attr is truthy!')
```
{{% /codeblock %}}





{{% tip %}}
**Additional notes**
- When opening text files for writing or appending text, use [`open`](https://docs.python.org/2/library/functions.html)'s option `mode = "wb"` or `mode  =  "ab"` respectively to  write in binary mode. This improves portability across operating systems.
-  When opening text files for reading, use [`open`](https://docs.python.org/2/library/functions.html)'s option `mode = "rU"` to enable universal newline support.
{{% /tip %}}

#### Supplemental resources:

- [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/), especially the sections on [coding style](http://docs.python-guide.org/en/latest/writing/style/) and [packaging conventions](http://docs.python-guide.org/en/latest/writing/structure/).
- [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html), especially recommendations concerning [string formatting](https://google.github.io/styleguide/pyguide.html#Strings) and the rule to always explicitly close [files and sockets](https://google.github.io/styleguide/pyguide.html?showone=Files_and_Sockets#Files_and_Sockets).
