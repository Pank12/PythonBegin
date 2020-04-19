class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self, ide):
        ide.execute()

#ide = PyCharm()
#ide.execute()
#OR --- Se here we need ide object should get execute method (It doesn't method from which class), This is Duck type
ide=MyEditor()
ide.execute()
lap1 = Laptop()
lap1.code(ide)

