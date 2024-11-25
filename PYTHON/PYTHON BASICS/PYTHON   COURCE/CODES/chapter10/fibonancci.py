# This is using recurssion method 
def fibonancci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonancci(n-1)+fibonancci(n-2)
number=(int(input("Enter the number:")))
print("Given fibonancci number is:",fibonancci(number))


# This is using Itteration
# def fibonancci(n):
#     prevNum=0
#     currentNum=1
#     for i in range(1,n):
#         PrevprevNum = prevNum
#         prevNum = currentNum
#         currentNum = prevNum +PrevprevNum
#     return currentNum


