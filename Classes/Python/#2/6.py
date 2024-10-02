# 6. Write a program that takes a string as input and prints its reverse.
def reverse_string(old_string):
    answer = ""
    for char in old_string:
        answer = char + answer
    return answer


user_input = input("Type something to be reversed\n")
# print(user_input[::-1])
print(reverse_string(user_input))
