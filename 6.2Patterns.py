# Pattern1
for i in range(1, 5):
    print(i," ", end="")
    for j in range(i+1, 5):
        print(j," ", end="")
    print()

# OR
string = '1234'
for i in range(len(string)):
    print(string[i:])

# Pattern2
print()

string1 = 'APQR'
string2 = 'ABCD'
for i in range(len(string1)):
#    print (i)
    string1 = string1.replace(string1[i], string2[i])
    print(string1)

# If the number is prime:
print()
a=10
#a=input("Please enter a value to check: ")
for i in range(2, a):
    if a%i == 0:
        print("Number is not a prime")
        break
else:
    print("Prime")