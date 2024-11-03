def My_func1(a,b):
    sum1 = a+b
    print(sum1) 

def update(original_func):
    def My_func2(*args):
        My_func1(*args)
        a,b = args
        print((a+b)**2)
    return My_func2

My_func_1 = update(My_func1)
My_func1(2,4)
My_func_1(3,5)