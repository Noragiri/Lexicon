# 2.
# Understand how to use filter() in Python with a lambda function to select elements from a list that meet a certain condition.
# Task:
# Explain what filter () does in Python and what kind of result it returns.
"""
The filter() function in Python takes two arguments: a function and an iterable (like a list or tuple). 
It applies the function to each item in the iterable, and returns an iterator that contains only the items for which the function returns True.
"""
# Create an example scenario where you need to filter out elements from a list.
"""
Scenario: Filtering out failed exam scores (below 50) from a list of student scores.
"""
# For instance, you are given a list of numbers, and you need to keep only the even numbers. How would you approach this using filter ()?
numbers = range(100)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
