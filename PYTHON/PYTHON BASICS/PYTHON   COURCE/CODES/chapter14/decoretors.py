# def func1():
#     print("Sudarshan sutar")

# func2=func1
# del func1
# func2() # if I have deleted the func1 after that also  I can retrive funct1 as funct1 value is already assigned in func2

# we can print built in function inside function
# def func1(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a=func1(0)
# print(a)
# we can take functions as parameter of another function
# def fun1(func):
#     func("This is python tutorial")
# fun1(print)


# ************Decorators*********
# I can pass a function as a parameter using decorators
def dec1(funct1):
    def executor():
        print("Execute now")
        funct1()
        print("Executed")
    return executor
def sudarshan():
    print("This is sudarshan sutar")
sudarshan = dec1(sudarshan)
sudarshan()
print("Another method is @ method")
@dec1
def sudar():
    print("Come on")
sudar()
