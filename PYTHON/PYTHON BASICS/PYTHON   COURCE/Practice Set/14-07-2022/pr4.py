# a=int(input("Enter a number:"))
# if a % 2 ==0:
#     print("The number is even")
# else:
#     print("The number is odd")


# x=int(input("Enter a number:"))
# if x in  range(1,10):
#     print("The given value is in between 1 and 10")
# else:
#     print("The given value is not in between 1 and 10")


# x=int(input("Enter a number:"))
# if x<0:
#     print("The given number is negative")
# elif x==0:
#     print("The given number is zero")
# else:
#     print("The given number is positive")

# printing even numbers between m and n

# m,n=[int(x) for x in input("Enter two numbers:").split(",")]

# x=m
# if x%2 !=0:
#     x=x+1

# while x>=m and x<=n:
#     print(x)
#     x=x+2

# l=[10,23,34,87,56,50]
# sum=0
# for element in l:
#     sum=sum+element
    
#     sum=sum+1
# print(sum)

# for i in range(4):
#     for j in range(5):
#         print("i=",i,"\t","j=",j)

# for i in range(1,11):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(1,11):
#     print("*"*(i))

# n=int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

i=0
while i<10:
    i+=1
    if i>5:
        continue
    print(i)


x=int(input("Enter a even number number:"))
try:
    assert x%2==0
    print("You have entered even number")
except:
    print("Wrong input entered")


