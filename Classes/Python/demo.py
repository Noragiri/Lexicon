x = int(input())
y = int(input())
z = int(input())
n = int(input())
cubes = [
    [a, b, c]
    for a in range(x + 1)
    for b in range(y + 1)
    for c in range(z + 1)
    if sum([a, b, c]) != n
]


print(cubes)
# print([sum(cube) for cube in cubes])
# print([cube for cube in cubes if sum(cube) != n])


# import string

# # alphabet = string.ascii_letters
# 87 - 122
# stringVariable = "0125abgtya"

# alphabet_a = list(map(chr, range(ord("a"), ord("z") + 1)))
# alphabet_b = list[map(chr, range(ord("a"), ord("z") + 1))]
# # alphabet = [chr(x) for x in range(ord("a"),ord("z")+1)]

# # for x in range(ord("a"),ord("z")+1)


# # map(function,itterator)


# print(alphabet_a)
# print(alphabet_b)
