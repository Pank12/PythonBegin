
#Global: it creates a global variable even you are withing the function
#Globals: this fetch the all the global variables, so you can use and you can update

a=10
print(id(a))

def something():
    #global a   #this will maje every a variable as a global(So will be never able to use "a" as a local variable)
    a=9
    x=globals()['a']    # I am specifing a as my nees, else it will give all the global variable
    print(id(x))

    print(id(a))
    print("in fun var: ", a)
    print("Global variable a fetching in fun: ",x)

    globals()['a']=15   #Updates global variable value
    print(id(a))


print("Outside global var: ",a)
something()


