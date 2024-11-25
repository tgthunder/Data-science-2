str=[]
n=int(input("How many strings you want:"))
for i in range(n):
    print("Enter string:")
    str.append(input())

str1=sorted(str)
print("Sorted list is:")
for i in str1:
    print(i)
