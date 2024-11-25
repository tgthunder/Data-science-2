#7. Write a program to print the multiplication table of a given number.

user_input = int(input("Enter number: "))

for i in range(1,11):
    print(f"{user_input}*{i} = {user_input*i}")
    