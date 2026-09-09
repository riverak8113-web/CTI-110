# Kaiden Rivera
# 09/8/2026
# P1HW1
# This program will calculate exponents of a base value that the user inputs, and add two integers together while subtracting the sum of those integers.

print("-----Calculating Exponents-----")
print()
a = int(input('Enter an integer as the base value: '))
b = int(input('Enter an integer as the exponent: '))
result1 = a**b

print(a, " raised to the power of ", b, " is ", result1, "! !")
print()

print("-----Addition and Subtraction-----")
print()
c = int(input('Enter a starting integer: '))
d = int(input('Enter an integer to add: '))
e = int(input('Enter an integer to subtract: '))
result2 = ((c+d)-e)

print(c, " + ", d, " - ", e, " is equal to ", result2)
