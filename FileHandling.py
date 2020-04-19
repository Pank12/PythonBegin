
f=open('MyData.txt', 'r')

#print(f.readline(), end='')
#print(f.read())
NewFile = open('MyDataNew.txt', 'w')
NewFile.write("Hello New file \n")

for data in f:
    NewFile.write(data)

# To copy a image

f1= open('imagename.jpg', 'rb')
f2= open('Newimagename.jpg', 'wb')
for i in f1:
    f2.write(i)
