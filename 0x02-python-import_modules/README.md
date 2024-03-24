0x02. Python - import & modules

In Python, the import statement is used to bring code from one module or package into another, enabling you to reuse code and create a more organized structure for your programs1.

When you import a module, Python searches for the module initially in the local scope by calling the __import__() function2. The value returned by the function is then reflected in the output of the initial code2.

A module in Python is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended3. Definitions from a module can be imported into other modules or into the main module3.

For example, if you have a module named fibo.py with functions fibo.fib(n) and fibo.fib2(n), you can import this module in another Python script using the command import fibo3. After importing, you can access the functions as fibo.fib(1000) and fibo.fib2(100)3.

If you intend to use a function often you can assign it to a local name: fib = fibo.fib3. Now you can call the function as fib(500)3.

In summary, the import statement and modules are fundamental concepts in Python that allow for code reuse and organization. They are crucial for building maintainable and modular applications, as they prevent code duplication and encourage the separation of concerns1.
Learning Objectives
Why Python is Awesome:
Python is like a Swiss Army knife for programmers. Here’s why:
General Purpose: You can create any kind of software with Python—whether it’s desktop applications, web services, or even embedded software using MicroPython.
Beginner Friendly: Python’s syntax is straightforward, making it easy for beginners to get started.
Thriving Community: Python boasts one of the largest and most active communities on platforms like Stack Overflow.
Career Opportunities: Python skills are highly sought after, with salaries ranging from $40,000 to over $100,000 annually1.
Importing Functions from Another File:
Suppose you have a Python file called my_functions.py with some useful functions. To use them in another file:
Python

# In your main script (e.g., main.py)
from my_functions import my_function1, my_function2

result1 = my_function1()
result2 = my_function2()
AI-generated code. Review and use carefully. More info on FAQ.
Creating a Module:
A module is a Python file containing functions, classes, or variables. To create a module:
Write your functions or code in a .py file (e.g., my_module.py).
Import it in other scripts using import my_module.
Using Imported Functions:
Once you’ve imported a module, you can call its functions directly:
Python

# In your main script
import my_module

my_module.my_function()
AI-generated code. Review and use carefully. More info on FAQ.
Using the Built-in Function dir():
The dir() function returns a list of all attributes (methods, functions, variables) of an object or module:
Python

dir(my_module)  # Lists all attributes in my_module
AI-generated code. Review and use carefully. More info on FAQ.
Preventing Code Execution When Imported:
Use the if __name__ == "__main__": guard to ensure that code within it runs only when the script is executed directly (not when imported as a module):
Python

# In my_module.py
def my_function():
    # Your code here

if __name__ == "__main__":
    # Code to run when script is executed directly
    print("This won't run when imported.")
AI-generated code. Review and use carefully. More info on FAQ.
Command Line Arguments in Python:
You can access command line arguments using the sys.argv list or the argparse module:
Python

import sys

# Example using sys.argv
script_name = sys.argv[0]
arg1 = sys.argv[1]
AI-generated code. Review and use carefully. More info on FAQ.
For more complex argument handling, consider using argparse:
Python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="Input file path")
args = parser.parse_args()

input_file = args.input

Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc

