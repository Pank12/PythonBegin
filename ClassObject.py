class Computer:

    def config(self):
        print("i5, 16gb, 1TB")

com1 = Computer()
com2 = Computer()

# This is the way to call the method, dot the particular object (com1 is going at the place of 'self')
Computer.config(com1)
Computer.config(com2)

# This is how we usualy use in python. Here indirectly in runtime com1 is going at the place of 'self'
com1.config()
com2.config()