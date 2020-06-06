'''
Write a Python program to get a dictionary from an object's fields.
'''
class a():
    def __init__(self):
        self.x=1
        self.y=2
    def func(self):
        print(self.x,self.y)
b=a()
b.func()
print(b.__dict__)