# 4.
# Learn how to combine the functionality of  filter() and map() to both select and modify elements in a list.
# Task:
# Describe a scenario where you need to filter out unwanted elements from a list and then modify the remaining elements.
# For example, you might first filter a list to keep only positive numbers, and then square those numbers.
# Break down the process of applying filter () first, and then using map() on the filtered result.

"""
Scenario:
You have a list of integers, and you want to filter out only the positive numbers and then square them.

Process Breakdown:
Filter: First, you apply filter() to remove unwanted elements (negative numbers and zeros). The function checks each element to see if it's greater than zero.
Map: After filtering, you use map() to modify the remaining elements (square the positive numbers).
"""

numbers = [-3, 0, 4, -1, 9, -5, 2]

# Step 1: Filter to keep only positive numbers
positive_numbers = filter(lambda x: x > 0, numbers)

# Step 2: Square the filtered positive numbers
squared_numbers = map(lambda x: x**2, positive_numbers)

# Convert to list to see the result
result = list(squared_numbers)
print(result)  # Output: [16, 81, 4]
