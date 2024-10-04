# 5.
# Understand Python’s scope rules and how they affect variable lookup and access in different contexts.
# Task:
# Explain the LEGB rule: Local, Enclosing, Global, Built-in.
# Describe what happens to a variable when it is defined:
# Inside a function (local)
"""
A variable defined inside a function is local to that function. 
It can only be accessed within that function, and it is created when the function is called and destroyed when the function exits.
"""
# Inside a function within another function (enclosing)
"""
A variable defined inside an outer function, and used in an inner function, is enclosing (or non-local).
It's accessible to the inner function but is not global.
"""
# In the main body of the program (global)
"""
A variable defined at the top level of a script or outside any function is a global variable. 
It is accessible throughout the program, including within functions (unless shadowed by a local variable of the same name).
"""
# As a built-in function (built-in)
"""
A built-in variable or function is provided by Python itself (like len(), print()). 
These are globally available throughout your program without needing to be defined by the user.
"""
# Example:
# Imagine you have a variable called x that exists in the global scope and is also redefined inside a function.
# Explain how Python resolves which value of x to use at different points in the program.

x = 10  # Global variable


def my_function():
    x = 20  # Local variable
    print(x)  # Refers to the local x inside the function


my_function()
print(x)  # Refers to the global x outside the function
