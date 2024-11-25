# Dictonaries
x = {"sudarshan":"python","Sourabh":"Java","Tanish":"C"}
print(type(x))
print(x.get('sudarshan'))
del x['Tanish']
print(x)
x['Sanket'] = "sql"
print(x)
x.update({"sudarshan":"Excel"})
print(x)
print(x.keys())
print(x.values())
y=[1,4,6,79,45,6]
x.update({"Values":y})
print(x.get("Values"))
print(x.items())

# sets 
set1 = {1,3,56,8,65}
print(type(set1))
set2 = {3,4,6,8}
print(set1.union(set2))
print(set1.intersection(set2))