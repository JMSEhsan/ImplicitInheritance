#Shaw, Zed, "Learn Python 3 The Hard Way" Addison-Wesly, 2017

class Parent(object):
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()