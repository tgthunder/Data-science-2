#5. Implement a program that converts temperature between Celsius and Fahrenheit scales.

def Cel_to_Far(n):
    n = (n* (9/5) )+ 32
    return n

print(Cel_to_Far(34))