# For Modules i am using this as a module.

def add():
    print("result 1 is :", __name__)

def sub():
    print("result 2 is ")

def main():
    print("in Calc main")
    add()
    sub()

if __name__ == "__main__":     # In this module if we use this line then when other module will call this module they will get that particular function (not whole module, even they want a fingle function from this module.)
    main()