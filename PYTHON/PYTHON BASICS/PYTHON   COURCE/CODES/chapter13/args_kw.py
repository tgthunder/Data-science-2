# use of args and kwrgs
# Many times you want to pass different numbers of arguments to a function
# At this time we have one option that to create functions for each input
# And another method is to pass *argumnets--> arbitrory positional arguments
# All the inputs passed by users will be packed in tuple....

def add(*args):
    sum = 0
    for i in args:
        sum+=i
    print(f"The sum is {sum}")

add(1,3,4,6,7)
add(34,10)

# We Can Pass Normal arguments As well with *args
# Order should be 1.Normal arguments then *args

print("-----------------------")
def add_norm(a,*numbers):

    print(a)
    print(numbers)
    sum = 0
    for i in numbers:
        sum+=i
    print(sum)

add_norm(1,34,7)
print("----------------------------------")
add_norm(20,10,12,14,16)

# We can pass different numbers of key value pairs and print them
# **kwargs --> Arbitrary key word arguments
# All the input is packed in a dictonary

def person_info(**kwargs):

    for k , v in kwargs.items():
        print(f"Key is: {k} and Value is: {v}")
    
person_info(name="Shyam",Age=30,dep="CSE")
person_info(name="Ram",dep="ENTC")

# Order --> Normal arguments,Non-keworded , Key-Worded