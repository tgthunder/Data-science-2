# def funct1(func):
#     def executor():
#         print("Execute now")
#         func()
#         print("Executed")
#     return executor
# def sudarshan():
#     print("This is sudarshan sutar")
# sudarshan=funct1(sudarshan)
# # sudarshan()

# @funct1
# def sudar():
#     print("Hi sudarshan ")
# sudar()




# def dec1(fun):
#     def inner():
#         value=fun()
#         return value+2
#     return inner

# @dec1
# def num():
#     return 10

# print(num())

def dec1(func):
    def inner():
        value=func()
        return value+2
    return inner

def dec2(func):
    def inner():
        value=func()
        return value*2
    return inner

@dec2
@dec1
def num():
    return 10

print(num())