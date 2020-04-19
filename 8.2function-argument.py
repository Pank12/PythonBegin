
def person(name, age):
    print(name)
    print(age)

person('Pankaj', 29)    # You have to carefull with sequence
person(age=29, name='Pankaj')    #When you are using keywords, you can change the sequence of argument passing

# Case2: def person(name, age=18):   #in this case you will not pass the argument when you are calling it, it will
        # bydefault take default value(here its 18), if you will pass it will take the new passed value.
# Case3: Variable length (eg *b):  number of argument will not be fixed. b will be as a tuple
def sum(a, *b):
    print(a)
    print(b)
    c=a
    for i in b:
        c=c+i
    print("sum = ",c)

sum(5,6,34,78)

#Case3: **kwargs: Keyworded variable length arguments (eg: **b)
def person1(name, **data):
    print(name)
#    print(data)    # this is the normal print of tuple
    for i,j in data.items():    # This is how you print dictionary
        print(i,j)

person1('Pankaj',age=29,city='Pune', mob=8975584)