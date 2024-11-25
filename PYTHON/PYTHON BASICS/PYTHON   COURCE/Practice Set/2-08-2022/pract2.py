# 2. Create a program that generates a list of even numbers within a given range.

l = []

a,b = [int(x) for x in input("Specify the range: ").split(" ")]

for i in range(a,b+1):
    if i%2 == 0:
        l.append(i)

print(l)