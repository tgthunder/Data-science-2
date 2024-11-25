#crate a list and print only numbers which are grater than 6
l=["sudarshan","google",4,"s",75,34,"apple",6]
for item in l:
    if str(item).isnumeric() and item>6:
        print(item)