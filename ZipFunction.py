names = ['Pankaj', 'Rahul', 'MP']
comp = ['Vaal', 'AllScript', 'Nice']

zipped = zip(names, comp)
zipped1 = list(zip(names, comp))
zipped2 = set(zip(names, comp))
zipped3 = dict(zip(names, comp))
print(zipped1)
print(zipped2)
print(zipped3)

for (a,b) in zipped:
    print(a,b)