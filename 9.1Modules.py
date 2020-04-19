from Calc import add

def fun1():
    add()       # We will get only add function(that we want), because Calc have (if __name__ == "__main__":)
    print("From fun1")

def fun2():
    print("From fun2")

def main():
    fun1()
    fun2()

main()