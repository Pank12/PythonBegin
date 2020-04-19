class Car:
    wheels = 5          # Class Variable/Static Variable

    def __init__(self):
        self.mil = 8            # Instance Variable
        self.comp = 'BMW'

c1 = Car()
c2 = Car()

c1.mil=10           # This change will only reflect in particular object (Instance)
Car.wheels = 10     # if you update class variable, it will change to all the objects

print(c1.mil, c1.comp, c1.wheels)
print(c2.mil, c2.comp, c2.wheels)