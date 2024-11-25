# 1. Write a Python program that takes two numbers as input and performs basic arithmetic operations (sum, difference, product, quotient).
a,b = [int(x) for x in input("Enter 2 numbers sep by space: ").split(" ")]

print(f"{a}+{b} = {a+b}")
print(f"{a}-{b} = {a-b}")
print(f"{a}*{b} = {a*b}")
print(f"{a}/{b} = {a/b}")