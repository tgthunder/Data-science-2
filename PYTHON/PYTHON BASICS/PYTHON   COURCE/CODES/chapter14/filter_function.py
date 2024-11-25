# filter is used to check conditions
l=[2,4,65,7,6,8,34,3]
def is_greater_5(a):
    return a>5
greater_5=list(filter(is_greater_5,l))
print(greater_5)


