#3. Develop a program that checks if a given number is prime or not.

def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1

user_input = input("Enter number: ")
user_input = int(user_input)

if is_prime(user_input):
    print("Prime")
else:
    print("Not a prime")