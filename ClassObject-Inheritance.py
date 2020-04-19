class A:
    def __init__(self):
        print("In init A")
    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 Working")

class B:

    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 Working")

class C(A,B):       # Multiple Inheritance
    def __init__(self):
        super().__init__()      # In this Method Resolution Order (MRO) (It execute from left to right, So A is first) will come in picture, so it will print only Class A's constructor followed by its own
        print("In init C")

    def feature6(self):
        print("Feature 6 Working")

class D(A):     # # Inheriting class A in B (Single Inheritance)
    def __init__(self):
        super().__init__()  # This will help to print super class's (Class A's) constructor before this (__init__(self) constructor, when we will call class(B))
        print("In init D")
    def feature5(self):
        print("Feature 5 Working")

class E(D):  # Multilevel Inheritance
    def feature7(self):
        print("Feature 7 Working")
a1=A()
a1.feature1()
b1=B()
b1.feature3()
e1=E()
e1.feature7()
d1=D()
d1.feature1()     #This is because of inheritance, we are able to access all the method of class A
c1=C()
c1.feature1()
c1.feature4()