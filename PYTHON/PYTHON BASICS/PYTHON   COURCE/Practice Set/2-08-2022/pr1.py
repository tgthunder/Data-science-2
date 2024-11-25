# check number is prime or not
# check if a string palindrome or not
# print fibonacci series
# check if all the numbers in a list are prime number or not 
# using a function
# make a list of 50 integer values print the number of occurences 
# of the series provided by user 

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1

# if is_prime(10):
#     print("number is prime")
# else:
#     print("Not a prime")


# def is_palindrome(str):
#     start = 0
#     end = len(str)-1
    
#     while(end>=start):
#         if (str[start] == str[end]):
#             start+=1
#             end-=1
#         else:
#             return 0
#     return 1

        

# if is_palindrome("sudarshan"):
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# def fibo(n):
#     a = 0
#     b = 1
#     print(a,b , end = " ")
#     for i in range(n):
#         nextnum = a+b
#         a = b
#         b = nextnum
#         print(nextnum , end= " ")

# fibo(5)


# num = int(input("Enter how many numbers you want: "))

# l = []

# for i in range(num):
#     n = int(input("Enter number: "))
#     l.append(n)

# for i in l:
#     if is_prime(i):
#         print(f"{i} is prime")
#     else:
#         print(f"{i} not a prime")


pred_list = [23,19,40,27,45,37,12,16,16,34,23,50,11,37,18,2,49,45,33,27,34,37,38,44,15,17,32,31,36,45,10,11,8,4,3,19,28,39,48,41,20,18,21,8,15,24,46,48,50,29]
print(len(pred_list))



print(pred_list)

user_list = []

n = int(input("How many numbers you want to add: "))

for i in range(n):
    num = int(input("Enter number: "))
    user_list.append(num)

print(user_list)

occurence = {}

for i in user_list:
    count = 0
    for j in pred_list:
        if i==j:
            count+=1
    occurence[i] = count

print(occurence)


        