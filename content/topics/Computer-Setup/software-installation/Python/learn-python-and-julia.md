---
title: "Get Started With Python"
description: "Learn how to program in Python."
keywords: "python, data science, data, programming, manipulation, analysis, tutorial"
draft: false
weight: 3
author: "Valerie Vossen"
aliases:
  - /learn/python
  - /python
---

## Overview

We introduce you to [Python]((https://www.python.org/)), starting with the fundamental basics to help you begin experimenting with this cool programming language yourself! Once you understand these essentials, the opportunities of Python are almost infinite. This guide covers: 

- Variables
- Data types
- Operators
- Functions
- Loops

{{% tip %}}

If you haven't installed Python yet, refer to our [Set up Guide](/install/python)
{{% /tip %}}

## Variables

Variables can only be one word and can contain letters, numbers, and underscores. They cannot begin with a number but can have numbers elsewhere in the name. Names are case-sensitive (`myVar` is different from `myvar`). It's common in Python to use underscores to separate words in variable names, for example: `user_name`, `total_count`, `my_groceries`. Choose meaningful and descriptive names for variables to enhance code readability. Some examples are: 

{{% codeblock %}}
```python
groceries_week12 = 123.49
total_count = 52
user_name = "Ellis"
```
{{% /codeblock %}}

## Data types
Python offers several built-in data types. The 4 basic types are **Numeric, String, Boolean, and Sequence data types**

1. **Numeric types**

This type holds numeric values, and has three different classes:
- Integers (`int`): whole numbers without decimal points
- Floating-point numbers (`float`): numbers with decimal points
- Complex numbers  (`complex`): numbers with a real and imaginary part

{{% codeblock %}}
```python

integer_var = 2
float_var = 2.24
complex_var = 1 - 2j #j is the imaginary unit 

# find out which data type your variable is:
print(type(integer_var))
```
{{% /codeblock %}}

Python returns `int`, as expected.

2. **String type**

Text values are composed of a sequence of characters. To convert another data type to a string, use `str()`.

{{% codeblock %}}
```python

my_string = "One apple costs "
my_string_2 = " Dollar"
x = 1

print(my_string + str(x) + my_string_2)
```
{{% /codeblock %}}

Output:

```python
One apple costs 1 Dollar
```

3. **Boolean types**

Boolean types are True or False values (the first letter is a capital letter!).


{{% codeblock %}}
```python

my_boolean = True
x = False

```
{{% /codeblock %}}

4.  **Sequence types**

A sequence data type holds a collection of data types. E.g.
- string (`str`) for representing text. Either single or double-quotes work.
- `list` for ordered and *mutable* sequences of elements.
- `tuple` for ordered and *immutable* sequences of elements.

Note that a list and tuple can hold different types of data! Examples of how to create a string, list, or tuple:

{{% codeblock %}}
```python

my_string = "Becoming a Python pro" 
my_list = [1, 2, 3.5, "Hello, you!"]
my_tuple = (4, 5.2, "Bye") 

```
{{% /codeblock %}}


### List methods

{{% codeblock %}}
```python

# sorted
x = [3, 1, 4, 1, 5]
sorted_list = sorted(x)
print(sorted_list)
```
{{% /codeblock %}}

Returns sorted copy of the list x:

```python
[1, 1, 3, 4, 5]
```

Selecting list elements. First element has index 0. 

{{% codeblock %}}
```python
# Select the 0th element in list
x[0] # returns 3

# Select the last element 
x[-1] # returns 5

# Select 1st (inclusive) to 3rd (exclusive) element
x[1:3] # returns [1, 4]
```
{{% /codeblock %}}

Concentenate lists with +

{{% codeblock %}}
```python
x = [3, 1, 4, 1, 5]
y = [4, 5, 6, 7, 8]
x + y 
```
{{% /codeblock %}}

Output:

```python
[3, 1, 4, 1, 5, 4, 5, 6, 7, 8]
```


### Dictionaries

A dictionary is an ordered collection of `key`: `value` pairs. E.g.

{{% codeblock %}}
```python
pancakes = {
    'flour': '2 cups',
    'milk': '1 1/2 cups',
    'eggs': '2',
}

```
{{% /codeblock %}}

Add an extra ingredient (new `key`: `value` pair) like this:

{{% codeblock %}}
```python
pancakes['baking powder'] = '2 teaspoons'
pancakes
```
{{% /codeblock %}}

```python
{'flour': '2 cups',
 'milk': '1 1/2 cups',
 'eggs': '2',
 'baking powder': '2 teaspoons'}
```

Get value with `[]`

{{% codeblock %}}
```python
pancakes['eggs'] #returns 2
```
{{% /codeblock %}}

Get all values with `values()`, and get all keys with `keys()`.

{{% codeblock %}}
```python
pancakes.values()
```
{{% /codeblock %}}

*Output:*
```python
dict_values(['2 cups', '1 1/2 cups', '2'])
```

Remove an item with `del()`.

{{% codeblock %}}
```python
del(pancakes['baking powder'])
pancakes
```
{{% /codeblock %}}

```python
{'flour': '2 cups',
 'milk': '1 1/2 cups',
 'eggs': '2'}
```

## Operators

### Math operators

The most basic math operators are:

{{% codeblock %}}
```python

addition = 5 + 3 
subtraction = 7 - 4
multiplication = 2 * 6
division = 9 / 2 
# return 4.5

floor_division = 9 // 2 
# return 4; largest integer less than or equal to the result

modulus = 10 % 3 
# return 1; remainder of division

exponentiation = 2**3 
# return 8

```
{{% /codeblock %}}

### Assignment operators

Assignment operators are used to assign values to variables, they combine the assignment of a value with an operation. The most commonly used are:

{{% codeblock %}}
```python

x = 5
x += 3    # equivalent to x + 5, result is 8

y =  6
x -= 2    # result is 4

a = 3
a /= 2    # result is 1.5

b = 3
b //=2    # result is 1

c = 11
c %= 5    # result is 1

e = 5
e *= 3    # result is 15

d = 4
d **=2    # result is 16

```
{{% /codeblock %}}

### Numerical comparison operators

Numerical comparison operators are used to compare values and return a Boolean result (`True`/`False`).

{{% codeblock %}}
```python

3 == 3 # Test for equality; returns True

3 != 3 # Test for inequality; returns False

3 > 1 # Greater than

3 >= 3 # Greater than or equal to

3 < 4 # Less than 

3 <= 4 # Less than or equal to
```
{{% /codeblock %}}


## Functions

### Define a function

Define a function with `def`, followed by the function name and parameters used in the function. It returns the function body (`x - y` after `return` on the second line).

{{% codeblock %}}
```python

# define function
def subtraction(x, y):
   return x - y

# call function
result = subtraction(3,6) 
print(result) # returns -3

```
{{% /codeblock %}}

#### Local or global variables

Global variables are defined outside any function and class and are accessible from any part of the code, useful for data that needs to be accessed from everywhere.

To modify a global variable from within a function, use the `global` keyword before the variable name to tell Python you are not creating a new local variable but are referring to the already existing global variable. Like this:

{{% codeblock %}}
```python

x_global = 10

# define function 
def modify_x(x_global):
  global x_global
  x_global /= 2

modify_x()
print(x_global) # returns 5

```
{{% /codeblock %}}

Variables defined inside a function or class are **local variables**. They can only be accessed from the function in which they are defined. 

{{% codeblock %}}
```python

def modify_x():
  x_local = 2             # local variable
  x_local = x_local + 2   # modify local var. inside function
  return x_local

result = modify_x()
print(result) 
# returns 4

print(x_local) 
# Raises error: x_local not possible to access outside function

```
{{% /codeblock %}}


### Lambda functions

Lambda functions are anonymous functions, meaning they don't have a name, like regular functions that are defined with `def`. They can have any number of arguments but are limited to a single expression. They are often used for quick one-off functions, where using an anonymous function prevents an overkill of function definition. For example, where a function is required as an argument of another function. In the example, the lambda function squares each element in the list.

The `map` function is used to apply the lambda function to each item in the `numbers` list.

{{% codeblock %}}
```python

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers)
print(squared) 
```
{{% /codeblock %}}

Output:

```python
[1, 4, 9, 16, 25]
```

### Built-in functions

Python has basic built-in functions, with some of the most commonly used functions:

| Function    | Description                                  |
|-------------|----------------------------------------------|
| `print()`   | Prints objects to the text stream            |
| `len()`     | Returns the length of an object              |
| `type()`    | Returns the type of an object                |
| `sum()`     | Sums start and the items of an iterable      |
| `max()`, `min()` | Returns the largest or smallest item in an iterable |
| `sorted()`  | Returns a new sorted list from an iterable    |
| `range()`   | Generates a sequence of numbers; range(start, stop, step). <br> By default starts from 0 and increments by 1, <br> and stops before a specified number          |
| `enumerate()` | Iterates over sequence and returns tuple <br> containing **index and corresponding element** from the iterable                  |
| `map()`     | Applies a function to every item of iterable  |
| `filter()`  | Selects elements from an iterable for which function returns True |
| `abs()`     | Returns the absolute value of a number       |
| `sum()`     | Adds all elements inan iterable and returns total      |
| `fsolve()`  | Finds the roots of a function numerically, <br> with function and initial guess added |
| `help()`    | Provides information about functions, classes etc.            |

Examples of the use of some of these functions:

{{% codeblock %}}
```python

# length and sum
length = len([1, 2, 3]) # returns 3
total = sum([1, 2, 3]) # returns 6

# max and min
max_value = max(4, 7, 2) # returns 7
min_value = min(4, 7, 2) # returns 2

# range(start, stop, step)
my_range = range(1, 10, 2)

# enumerate example
groceries = ['apples', 'milk', 'eggs']
enumerated_list = list(enumerate(fruits)) 
                #returns [(0, 'apples'), (1, 'milk'), (2, 'eggs')]

# map: apply lambda function to all elements in list
squared = list(map(lambda x: x**2, [1, 2, 3, 4, 5]))
                # returns [1, 4, 9, 16, 25]

# filter even numbers
even = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
                # returns [2, 4]

# fsolve
from scipy.optimize import fsolve
root = fsolve(lambda x: x**2 - 4*x + 4, 2.0)
                # returns array([2.])

# help
help(filter)
```
{{% /codeblock %}}

### List comprehension: alternative to filter

We have seen what a list is already, and how you can create one. List comprehension can be used as the often preferred alternative to the `filter` function, because it's more concise and better readable.

{{% codeblock %}}
```python

numbers = [1, 2, 3, 4, 5, 6]

# Using filter to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

# Using list comprehension to get even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)
```
{{% /codeblock %}}

Both approaches produce the same result: `[2, 4, 6]`, a list containing the even numbers from the original list. 

## Loops

### For loops

For loops are used to iterate over a sequence (such as a list, or range). For example:

{{% codeblock %}}
```python

# Iterating over a list
numbers = [1, 2, 3, 4, 5]

for x in numbers:
    print(x)

# Iterating over a range of numbers

for i in range(1, 6):
    print(i)

```
{{% /codeblock %}}

Both return this:

```python
1
2
3
4
5
```

### While loops

While loops repeat as long as a certain boolean condition is met. 

In the following example, a countdown is created by printing numbers from 5 to 1. *While* the number is above 0, the countdown keeps going and the statement of subtracting 1 of the number is repeated.

{{% codeblock %}}
```python

# Countdown using a while loop
countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

```
{{% /codeblock %}}

Output:

```python
5
4
3
2
1
```


### break, else,  and continue statements

1. break

The `break` statement is used to exit a loop prematurely based on a certain condition. In this example, we search for a specific number in a list, and break out of the loop as soon as it finds the right number.

{{% codeblock %}}
```python
numbers = [14, 23, 18, 5, 10]

right_number = 18

for number in numbers:
    print(f"Checking number {number}")
    
    if number == right_number:
        print(f"Found the right number: {right_number}!")
        break
```
{{% /codeblock %}}

Output:

```python

Checking number 14
Checking number 23
Checking number 18
Found the right number: 18!

```

2. `else`

The `else` block in a loop is executed when the loop condition becomes `False`. However, if the loop is terminated by a break statement, the `else` block is skipped. Here's an example:


{{% codeblock %}}
```python
numbers_2 = [14, 23, 5, 10]

right_number = 18

for number in numbers_2:
    print(f"Checking number {number}")
    
    if number == right_number:
        print(f"Found the right number: {right_number}!")
        break

    else:
        print(f"Number {search_for_number} is not found in the list.")
```
{{% /codeblock %}}

Output:

```python

Checking number 14
Checking number 23
Checking number 5
Checking number 10
Number 18 is not found in the list.

```

3. continue

The `continue` statement is used to skip the rest of the code inside a loop for the current iteration and move on to the next iteration. In this example, the `continue` statement skips the `print(number)` for even numbers. As a result, only the odd numbers in the list are printed. 

{{% codeblock %}}
```python

numbers = [14, 23, 18, 5, 10]

for number in numbers:
    if number % 2 == 0:
        # Skip even numbers
        continue
    
        print(number)

```
{{% /codeblock %}}

Output:

```python
23
5
```

{{% summary %}}

With the basics of Python under your belt, you're ready to start experimenting and expanding your skills. Check out these resources to further your learning:

- [Python Coding Style Guidelines](python/style-guides): Discover the importance of coding style with these essential guidelines.
- Learn Python with these great step-by-step tutorials from [Real Python](https://realpython.com).
- [QuantEcon.org](https://quantecon.org/) offers fantastic resources for you to
get started using Python.

In particular, we would like to refer you to their [open-source lectures](https://quantecon.org/lectures/), covering: [Quantitative Economics with Python](https://python.quantecon.org/), including a fantastic, open-source book companion, and [QuantEcon Data Science](https://datascience.quantecon.org/).

{{% /summary %}}
