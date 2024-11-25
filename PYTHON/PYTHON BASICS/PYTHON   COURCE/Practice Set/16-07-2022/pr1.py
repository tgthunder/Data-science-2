# file=open("samplefile.txt","w")
# a=file.write("Hi I am back")
# print(a)

# file=open("samplefile.txt","a")
# a=file.write("Hi I am back")
# print(a)


file=open("samplefile.txt","r+")
a=file.read(15)
print(a)
b=file.write(" Thank You")
print(b)

