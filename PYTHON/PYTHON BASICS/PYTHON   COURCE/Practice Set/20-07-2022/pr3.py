f=open("myfile.txt","w")

print("Enter the text @ the end ")

while str != "@":
    str=input()
    if(str!= "@"):
        f.write(str+"\n")
f.close()