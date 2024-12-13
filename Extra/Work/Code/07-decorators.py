def double(func):  
    def wrapper():  
        #func()  
        #func()  
        func()
    return wrapper    
@double
def f1():  
    print("Hello There")  
f1()