class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is :", self.cpu, self.ram)

com1 = Computer('i5', 16)
com2 = Computer('Ryzen 3',8)

print(id(com1))
print(id(com2))

# This is how we usualy use in python. Here indirectly in runtime com1 is going at the place of 'self'
com1.config()
com2.config()
