def decor(func):
    print(2)
    def wrapper(x):
        print(3)
        y = func(x)
        print(4)
        return x*y
    return wrapper

@decor
def output (x, optional="Hello World"):
    print(1)
    return x, optional


print(output(5))
#print (('Hello', 'World')*5)