# list comprehensions
# comprehensions means generate a list in a single line
# l1=[]
# for i in range(100):
#     if i%3==0:
#         l1.append(i)

# print(l1)

l=[i for i in range(100) if i%3==0]  # this is list comprehension
print(l)

# Dictionary comprehension
dict1={i:f"item{i}" for i in range(10)}
dict1={value:key for key,value in dict1.items()} # in this we can reverse the dictionary
print(dict1)

# set comrehension

dresses={dress for dress in ["dress1","dress2","dress2","dress1"]}
print(dresses)

# generator comprehensions
evens=(i for i in range(100) if i%2==0)
print(evens)
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())