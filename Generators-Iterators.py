def topten():

    n=1
    while n<= 10:
        sqr=n*n
        yield sqr       # This will load the values one by one in memory (So speed will be better)
        #print(sqr)     # this will load all the values once then will go for further processing
        n+=1

values = topten()

for i in values:
    print(i)