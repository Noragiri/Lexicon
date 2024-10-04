# 1.
# Understand what a lambda function is and when to use it in Python.
# Task:
# Research and explain what a lambda  function is.
"""
lambda is a way to create small, anonymous functions. 
"""
# Describe situations where using a lambda  function would be more appropriate than defining a full function using def.
"""
It is often used for functions that are simple enough to be defined in one line and are not needed more than once in a program.
"""
# Explain the following terms in relation to lambda:
# Anonymous function
"""
Anonymous function is lambda function assigned to variable. It can be called just like a function e.g. varName(args)
"""
notAFunctionWink = lambda x, y: x + y
print(notAFunctionWink(4, 5))
# Inline function
list = [1, 2, 3, 4, 5, 6]
print(map(lambda x: x * 2, list))
