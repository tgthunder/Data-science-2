try:
    file=open("myfile.txt","w")
    a,b=[int(x) for x in input("Enter two numbers:").split(",")]
    c=a/b
    file.write("writing %d into myfile" %c)

except ValueError:
    print("You divided the number by zero")
    print("Please enter valid input")

finally:
    file.close()
    print("File is closed")

for i in range(1,11):
    print(" *"*(i))



