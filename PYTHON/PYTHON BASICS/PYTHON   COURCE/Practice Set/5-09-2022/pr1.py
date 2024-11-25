# Dictionary , sets and further revision

d = {"name":"Sudarshan" , "Sal":1500 , "Post":"Data Entry"}

d1 = {101:["Sudarshan" , 1500 , "Manager"],
      102:["Sourabh" , 2000 , "Boss"]}

print(len(d1))
print(d1[102])
d["Gender"] = "M"

d1[102] = ["Nana" , 3400]

print(d1)
print(len(d1))
print(d1[102])

d.clear()

print(d)
d2 = d1

print(d2)

d2[103] = ["Tanish" , 1600 , "SDE"]

print(d1)

print(type(d1.items()))

print(d1.keys())

print(d1.values())