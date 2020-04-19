# Method Overriding
class A:
    def show(self):
        print("My father phone")

class B(A):
    def show(self):
        pass
        print("my own phone")

obj=B()
obj.show()
# Here inheretance will not make difference, because method name is same and object have its own value
#if only pass will be in class B' show method, then Cllass A's Show will give its value to Class B's show