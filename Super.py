#Shaw, Zed, "Learn Python 3 The Hard Way" Addison-Wesly, 2017

class Parent(object):
    
    def altered(self):
        print("Parent altered()")
        
class Child(Parent):

    def altered(slef):
        print("Child, before Parent altered()")
        super(Child, self).altered()
        print("Child, after parent altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()