# 3. Given a string, return a string where for every char in the original, there are two chars.


def doubleChar(str):
    answer = ""
    for ch in str:
        answer = answer + ch + ch
    return answer


print(doubleChar("The"))  #'TThhee'
print(doubleChar("AAbb"))  #'AAAAbbbb'
print(doubleChar("Hi-There"))  #'HHii--TThheerree'
