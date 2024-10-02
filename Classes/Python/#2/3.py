# 3. Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.
def even_tuple(input_tuple):
    temp_list = []
    for number in input_tuple:
        if number % 2 == 0:
            temp_list.append(number)
    new_tuple = tuple(temp_list)
    return new_tuple


print(even_tuple(tuple(range(10))))
