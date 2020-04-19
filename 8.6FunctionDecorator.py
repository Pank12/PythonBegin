def div(a,b):
    print(a/b)

#in abouve function we want to make a change from outside to take
# "a" as greater than b (so for that we will use decorator to swap)

def smart_div(f):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return f(a,b)
    return inner

div = smart_div(div)
div(2,4)