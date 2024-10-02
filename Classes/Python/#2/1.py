# 1. Write a program that takes two integers as input, base and exponent, and calculates the power using loops.
first_input = input("Input base:\n")
second_input = input("Input exponent:\n")
base = int(first_input) if first_input.isdigit() else None
exponent = int(second_input) if second_input.isdigit() else None
if base != None and exponent != None:
    power = 1
    while exponent >= 1:
        power = power * base
        exponent -= 1
    print(power)
else:
    print("Please input numbers")
