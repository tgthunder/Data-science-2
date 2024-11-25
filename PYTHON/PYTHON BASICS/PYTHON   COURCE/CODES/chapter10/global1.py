m=10   # this is global
def function1(n):
    a=5 
    # m=20   # these a and b are local variables which are inside function
    b=3
    # m=m+16   # we cant change the value of global variable inside function
        #we can change the value of global variable using global keyword
    global m
    m=m+10
    print(a,b,m)
    print(n,"My name is Sudarshan")
function1("I am here")  

def sudarshan():
    x=15
    def f2(): 
        global x  # we can not write global variable inside nested functions
        x=23     
    print("before calling f2",x) 
    f2()
    print("After calling f2",x)  
sudarshan()    

