
def greet():
    print("Hello")
    print("Good Morning")

def add(x,y):
    c=x+y
    return c

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result = add(5,2)       # this is how function return the values
print(result)
result1, result2 = add_sub(5,4)
print(result1, result2)
greet()                 #This type function doesn't return the value

