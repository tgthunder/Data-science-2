a=open("f1.txt")
try:
    f=open("f1.txt")

except Exception as e:
    print(e)

else:
    print("This is run when exception is not occured")
finally:
    print("This must be executed")

print("Important stuff")