# 1 . Given the string
s = "Python"
# Use indexning to print the following:
# Output:
# 'o'
print(s[4:5])
# 'Pyth'
print(s[:4])
# 'yth'
print(s[1:4])
# 'nohtyP
print(s[::-1])

# 2 . Given the nested list:
l = [3, 7, [1, 4, "hello"]]
# Reassign "hello" to be "goodbye"
l[2][2] = "goodbye"
print(l)

# 3 . Using keys and indexing, grab the 'hello'
# from the following dictionaries:
d1 = {"simple_key": "hello"}
print(d1["simple_key"])
d2 = {"k1": {"k2": "hello"}}
print(d2["k1"]["k2"])
d3 = {"k1": [{"nest_key": ["this is deep", ["hello"]]}]}
print(d3["k1"][0]["nest_key"][1][0])

# 4 . Use a set to find the unique values of the
# list below:
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
print(set(mylist))

# 5. You are given two variables:
age = 4
name = "Sammy"
# Use print formatting to print the following string:
print(f"Hello my dog's name is {name} and he is {age} years old")
