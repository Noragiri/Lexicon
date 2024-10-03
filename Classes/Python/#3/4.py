# 4. Return the number of even integers in the given array/list.
# Examples:


def count_evens(nums):
    even_count = len([num for num in nums if num % 2 == 0])
    return even_count


print(count_evens([2, 1, 2, 3, 4]))  # 3
print(count_evens([2, 2, 0]))  # 3
print(count_evens([1, 3, 5]))  # 0
