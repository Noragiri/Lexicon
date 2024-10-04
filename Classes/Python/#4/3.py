# 3.
# Learn how to use map() to apply a transformation to every item in a list.
# Task:
# Explain the purpose of map() and how it works in Python.
"""
The map() function in Python applies a given function to each item in an iterable (like a list or tuple) and returns an iterator with the results.
"""
# Create a real-life scenario where you need to modify every element of a list in the same way.
"""
Scenario: Price increase by percentage
"""
# For example, you have a list of prices, and you want to apply a 10% discount to each. How would you use map () with a lambda function to achieve this?
prices = [1.0, 2.0, 3.0, 4.0]
prices = list(map(lambda x: x * 0.9, prices))
print(prices)
