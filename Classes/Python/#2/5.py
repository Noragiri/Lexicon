# 5. Write a program that takes a list of integers as input and uses list comprehension to create a new list containing only the even numbers from the original list.
def even_list(list):
    return [number for number in list if number % 2 == 0]


user_input = input("Input a sequence of integers separated by comma (e.g. 1,2,3,4)\n")
try:
    input_list = list(map(int, user_input.split(",")))
    new_list = even_list(input_list)
    print(new_list)
except ValueError:
    print("Improper input")
