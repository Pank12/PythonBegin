# For loop
for i in range(1,21):
    if i%5 == 0:
        print(i)

# For else statement
print()
nums = [12, 16, 18, 21, 26]
for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("Not found")