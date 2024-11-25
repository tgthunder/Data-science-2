# Define a function that takes integer as an input and returns the square of the number
# Conditions: the number and the square should be integers 
# Cases: 10000
# 55
# 100000
# 9999999
# you should handle the upcoming exceptions accordingly

def sqaure():
    num = int(input("Enter Number: "))
    return num**2

print(sqaure())