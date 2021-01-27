<!-- This is a template. Please update the content while keeping this structure. We provide examples in the comments below. Make sure to read our contribution guide to learn how to submit your content to Tilburg Science Hub. -->

# Chapter Title

<!-- # How to check if a number is prime -->

Provide a brief overview of the issue to solve, or why this is a best practice. Explain the goal of this step and how it connected to the previous ones. Optionally, if you have assigned a task in the previous chapter, provide the solution at the beginning of this one.

<!-- Now that you've learned what is a prime number, you may be wondering how to tell if a number is prime. Let's write some code that will help you find it out. -->

## The task

Explain the solution step by step. If you can, record a video following our [video guidelines for Tutorials](). If there's code involved, explain small snippets first and add more to build the final code, which you can display at the end of the chapter.

<!-- In this program, we check whether the variable ```num``` is prime or not. Numbers less than or equal to 1 are not prime numbers. Therefore, we only proceed if the ```num``` is greater than 1. -->

### Step 1

#### Step 1.1

Use subheaders if needed.

<!-- We check if ```num``` is exactly divisible by any number from 2 to num - 1. If we find a factor in that range, the number is not prime. Else the number is prime]. -->


### Python <!-- Provide your code in all the relevant languages and/or operating systems. -->

```python
# program to check if a number is prime or not

num = 333

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number.")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number.")

# if num is less than or equal to 1, it is not prime
else:
   print(num,"is not a prime number.")
```

### Output
```python
333 is not a prime number
3 times 111 is 333
```

## Next steps

Explain briefly how to bring this to the next level, provide useful resources, and announce what will come in the following chapter.

<!-- Alternatively, instead of declaring ```num``` in the code, you can take input from the user. -->

```python
# to take input from the user
num = int(input("Enter a number: "))
```

<!-- Moreover, to make it more efficient, we can decrease the range of numbers where we look for factors.

For instance, we could have used the range ```range(2,math.floor(math.sqrt(num)))```. This is based on the fact that a composite number must have a factor less than the square root of that number. Otherwise, the number is prime.

You can learn more about prime numbers here and here, or follow our in-depth tutorial on Arithmetic programming for dummies. -->

## (Optional) Knowledge check

Challenge your audience with a small test, quiz or task. You can provide the (written or video) answer in the next chapter.
