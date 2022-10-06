#Shaw, Zed, "Learn Python 3 The Hard Way" Addison-Wesly, 2017

class Parent(object):
    def override(self):
        print("PARENT override()")

class Child(Parent):
    def override(slef):
        print("Child override")

dad = Parent()
son = Child()

dad.override()
son.override()