from array import *
# arrays operations
#1.accept marks from keyboard into a list

lst=[int(i) for i in input("Enter marks :").split(',')]
marks=array("i",lst)
sum=0
for i in marks:
    print(i)
    sum+=i
print("The sum of marks:",sum)

n=len(marks)
percentage=sum/n
print("Percentage of marks is:",percentage)