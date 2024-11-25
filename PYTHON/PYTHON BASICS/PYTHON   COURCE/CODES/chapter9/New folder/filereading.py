file=open("yes.txt")        #here open is used to open a file .txt file is mode    here file pointer will return opening of file
content=file.read()
print(content)
file.close()
# operations on file
# default mode 
f1=open("yes.txt","rt")   # this will read the file in binary mode/text mode
a=f1.read(4)       # this will read 4 characters
print(a)

a=f1.read(4)        # this will read next 4 characters
print(a)
f1.close()
#we can read file line by line
f2=open("yes.txt","rt")
for line in f2:
    print(line,end="")
