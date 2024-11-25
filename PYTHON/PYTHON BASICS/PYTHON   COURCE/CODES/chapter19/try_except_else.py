f1=open("ffsudarshan.txt")

try:
    a=open("does.txt")

except Exception as e:
    print(e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    f1.close()
    a.close()

print("Important stuff")