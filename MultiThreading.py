from time import *
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1=Hello()
t2=Hi()
#t1.run()   # In multithreading we cannt use method name to call
#t2.run()
t1.start()
sleep(0.2)      # To make in Async to t1 and t2
t2.start()
# Join is to be used to keep together both the threads
t1.join()
t2.join()
# This will be execute (print) after t1 and t2 thread execution will be completed
print("Bye")