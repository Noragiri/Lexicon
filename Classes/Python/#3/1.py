# 1. Given a list of integers, return True if the sequence of numbers 1, 2, 3 appears in the list somewhere.
# Example:
def arrayCheck(intArray):
    for x in range(len(intArray) - 2):
        if intArray[x] == 1 and intArray[x + 1] == 2 and intArray[x + 2] == 3:
            return True
    return False


print(arrayCheck([1, 1, 2, 3, 1]))  # True
print(arrayCheck([1, 1, 2, 4, 1]))  # False
print(arrayCheck([1, 1, 2, 1, 2, 3]))  # True
