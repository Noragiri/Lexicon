# 4. Write a program that merges two dictionaries into a single dictionary. If a key is common to both dictionaries, the value from the second dictionary should be used.
def merge_dictionary(dictionary_one, dictionary_two):
    new_dictionary = {}
    for key in dictionary_one:
        new_dictionary[key] = dictionary_one[key]
    for key in dictionary_two:
        new_dictionary[key] = dictionary_two[key]
    return new_dictionary


first_dictionary = {"one": 1, "two": 2, "three": 3}
second_dictionary = {"two": 22, "four": 44, "six": 66}

print(merge_dictionary(first_dictionary, second_dictionary))
