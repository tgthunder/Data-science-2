from pip import main

def string1(string):
    return f"This is python tutorial {string}"

def sub(a,b):
    return a-b+10
print("This is name function",__name__)

if __name__ =='__main__':
# using name as main we can not import all the executions after this
    print(string1("I like to code in python")) 
    c=sub(15,5) 
    print(c)

