# 2. Given a string, return a new string made of every other character starting with the first, so "Hello" yields "Hlo".
# Example:
def stringBits(input_string):
    return input_string[::2]


print(stringBits("Hello"))  #'Hlo'
print(stringBits("Hi"))  #'H'
print(stringBits("Heeololeo"))  #'Hello'
