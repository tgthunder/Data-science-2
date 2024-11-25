list1=["harry","Larry","Garry","Barry"]
print(list1[0],list1[1],list1[2],list1[3])
for i in list1: 
    print(i)
# Using for loop we can display repeate operations at one time
# we can do same with tuples
l2=[["harry",15], ["larry",12], ["garry",40], ["barry",4]]
for iteam in l2:
    print(iteam) #we can print list inside list
for iteam,samosa in l2:
    print(iteam,samosa) #we can unpack any list like this
dict1=dict(l2)
print(dict1)
print(type(dict1))
for iteam in dict1.items():
    print(iteam)         
for keys in dict1.keys():
    print(keys)    