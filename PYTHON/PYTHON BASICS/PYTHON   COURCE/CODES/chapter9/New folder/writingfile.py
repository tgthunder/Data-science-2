f=open("sudarshan2.txt","w")
f.write("I love my India ")
f.close()
#append
f1=open("sudarshan2.txt","a")
a=f1.write("I proud of my country\n")     #.write function will return no of characters
print(a)
f1.close()
# handle read and write both
f2=open("sudarshan2.txt","r+")
print(f2.read())
f2.write("Thank you")  
f2.close()