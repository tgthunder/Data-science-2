# tell,seek and more functions of file
f=open("darshan.txt")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
f.close()
f1=open("sudarshan.txt")
print(f1.readline())
f1.seek(10)  #seek function will reset your file line at position you want
f1.close()