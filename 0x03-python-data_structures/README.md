# 0x03. Python - Data Structures: Lists, Tuples
## Learning Objectives
###  Why Python programming is awesome
Python programming is awesome because of its simplicity and readability. It's easy to learn and use, making it great for beginners and experienced programmers alike. Python has a vast standard library and active community support, making it suitable for a wide range of applications, from web development to scientific computing.
 
###  What are lists and how to use them
Lists in Python are ordered collections of items. You can create a list by enclosing items in square brackets [] and separating them with commas. Lists can contain elements of different types and are mutable, meaning you can change their content after creation.
 
###  What are the differences and similarities between strings and lists
Strings are sequences of characters, while lists are sequences of any type of Python objects. Both strings and lists are ordered collections, meaning you can access their elements by index. However, strings are immutable, while lists are mutable.
 
###  What are the most common methods of lists and how to use them
Some common methods of lists include append(), extend(), insert(), remove(), pop(), index(), count(), sort(), and reverse(). These methods allow you to modify and manipulate lists in various ways.
 
###  How to use lists as stacks and queues
You can use lists as stacks (Last In, First Out) by using the append() method to add items to the end of the list and the pop() method to remove items from the end. For queues (First In, First Out), you can use the append() method to add items to the end of the list and the pop(0) method to remove items from the beginning.
 
###  What are list comprehensions and how to use them
List comprehensions provide a concise way to create lists in Python. They consist of an expression followed by a for clause and can optionally include if clauses. For example, [x**2 for x in range(5)] creates a list of squares of numbers from 0 to 4.
 
###  What are tuples and how to use them
Tuples are ordered, immutable collections of Python objects. They are created by enclosing items in parentheses () and separating them with commas. Tuples are often used to represent fixed collections of related data.
 
###  When to use tuples versus lists
Use tuples when you have a collection of items that should not change, such as coordinates or settings. Use lists when you need a collection of items that can be modified, such as a list of tasks.
 
###  What is a sequence
In Python, a sequence is an ordered collection of items. Strings, lists, and tuples are all examples of sequences.
 
###  What is tuple packing
Tuple packing is the process of creating a tuple by placing multiple items separated by commas. For example, my_tuple = 1, 2, 3 creates a tuple (1, 2, 3).
 
###  What is sequence unpacking
Sequence unpacking is the process of extracting individual items from a sequence (like a tuple or a list) into separate variables. For example, a, b, c = my_tuple unpacks the tuple my_tuple into variables a, b, and c.
 
###  What is the del statement and how to use it
The del statement is used to delete items from a list or variables from the current namespace. For example, del my_list[0] deletes the first item from my_list, and del my_variable deletes the variable my_variable.
 
## Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
 
## Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
## C
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
You are not allowed to use global variables
No more than 5 functions per file
In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
The prototypes of all your functions should be included in your header file called lists.h
Don’t forget to push your header file
All your header files should be include guarded
 
 
Task 0 
o-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer
 
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
 
0-print
#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for num in my_list:
        print("{:d}".format(num))
 
1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at
 
my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
 
1-element
#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
 
 
my_list = [1, 2, 3, 4, 5]
2-main
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list
 
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)
 
print(new_list)
print(my_list)
 
2-replace
 
#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
 
 
my_list = [1, 2, 3, 4, 5]
 
3-main
 
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer
 
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
 
3-reverse 
#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for num in reversed(my_list):
        print("{:d}".format(num))
 
# Example usage
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
 
lists.h
 
def print_list_integer(my_list=[]):
def element_at(my_list, idx):
def replace_in_list(my_list, idx, element):
def print_reversed_list_integer(my_list=[]):
 

