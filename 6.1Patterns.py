# Pattern-1
i=1
while i <= 4:
    print("# ", end="")
    j=1
    while j<=4:
        print("# ", end="")
        j+=1
    i+=1
    print()
print()         # For new line
# Pattern-1 in easy way
for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()
print()
# Pattern-2
for i in range(4):
    for j in range(i+1):
        print("# ", end="")
    print()
print()
# Pattern-3

for i in range(4):
    for j in range(4-i):
        print("# ", end="")
    print()