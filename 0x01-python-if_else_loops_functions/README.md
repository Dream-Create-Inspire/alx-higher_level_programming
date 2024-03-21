#0x01. Python - if/else, loops, functions

Learning Objectives
Why Python programming is awesome Python is an advanced, general-purpose programming language created by Guido van Rossum in 1991. Here’s why it’s awesome:

Versatility: Python can be used for anything—from web development to scientific research, artificial intelligence, and more. Beginner-Friendly: Its straightforward syntax makes it easy for newcomers to learn. Community Support: Python has a large and helpful community on platforms like Stack Overflow. Career Opportunities: Python developers are in high demand, with salaries ranging from $40,000 to over $100,000 annually1.

Why indentation is so important in Python In Python, indentation matters! It defines code blocks (such as loops and conditionals). Proper indentation ensures readability and correct program execution.

How to use the if, if ... else statements Conditional statements allow you to make decisions in your code. Here’s how to use them:

Python

if condition: # Code to execute if condition is True else: # Code to execute if condition is False

How to use comments Comments help explain your code. Use # for single-line comments and ''' or """ for multi-line comments.

Example:

Python

This is a single-line comment
''' This is a multi-line comment '''

How to affect values to variable Assign values using the = operator:

Python

my_variable = 42

How to use the while and for loops while loop: Repeats code while a condition is True. for loop: Iterates over a sequence (e.g., a list, tuple, or range). Example:

Python

while loop
while condition: # Code to repeat

for loop
for item in iterable: # Code to execute for each item

How is Python’s for different from C‘s? Python’s for loop is more like a “for-each” loop. It iterates directly over elements (not indices) in a sequence.

How to use the break and continues statements break: Exits a loop prematurely. continue: Skips the current iteration and moves to the next.
How to use else clauses on loops The else block in a loop executes when the loop completes all iterations (without encountering a break).

What does the pass statement do, and when to use it The pass statement does nothing. It’s a placeholder for future code. Use it when you need a syntactically valid empty block.

How to use range range(start, stop, step) generates a sequence of numbers. Example:

Python

for i in range(1, 6): print(i) # Prints 1 to 5

What is a function and how do you use functions A function is a reusable block of code. Define one using def:

Python

def greet(name): return f"Hello, {name}!"

result = greet("Alice") print(result) # Prints "Hello, Alice!"

What does return a function that does not use any return statement If a function doesn’t have a return statement, it implicitly returns None.

Scope of variables Variables have different scopes (local, global). Local variables exist within a function, while global variables are accessible throughout the program.

What’s a traceback A traceback is an error message that shows the call stack when an exception occurs. It helps identify where the error occurred.

What are the arithmetic operators and how to use them Arithmetic Operators and How to Use Them Python supports common arithmetic operators:

+: Addition -: Subtraction *: Multiplication /: Division %: Modulo (remainder) **: Exponentiation Example:

Python

result = 10 + 5 print(result) # Prints 15

Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. You are not allowed to publish any content of this project. Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
Python Scripts
Allowed editors: vi, vim, emacs All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5) All your files should end with a new line The first line of all your files should be exactly #!/usr/bin/python3 A README.md file, at the root of the folder of the project, is mandatory Your code should use the pycodestyle (version 2.8.*) All your files must be executable The length of your files will be tested using wc C Scripts

C Scripts
Allowed editors: vi, vim, emacs All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89 All your files should end with a new line Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl You are not allowed to use global variables No more than 5 functions per file In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples The prototypes of all your functions should be included in your header file called lists.h Don’t forget to push your header file All your header files should be include guarded

#More Info Note: you do not need to understand lists yet.

