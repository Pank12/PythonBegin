# Candy Bending machine
available=5
x = int(input("How many Candies you want?"))
i=1
while i <= x:
    if x >= available:
        print("Out of stock")
        break
    print('Candy')
    i+=1
print("Bye")

# Print which is not divisible by 3 or 5
for i in range(1,11):
    if i%3 ==0 or i%5 == 0:
        continue
    print(i)

print("Good Bye")

# Print odd values
for i in range(1,22):
    if (i%2 != 0):
        pass
    else:
        print(i)