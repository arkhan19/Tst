def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiplay(x, y):
    return x*y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot Divide by Zero")
    return x / y


print (add(1,2))