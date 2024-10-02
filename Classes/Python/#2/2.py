# 2. Write a program that calculates the sum of all elements in a given tuple.
def sum_tuple(tuple):
    sum = 0
    for number in tuple:
        sum += number
    return sum


print(sum_tuple((1, 2, 3, 4)))
