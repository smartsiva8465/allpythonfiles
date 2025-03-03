"""class Typesofmethod:
    x='class variable'
    def __init__(self):
        print('init method')
    def instance(self,y):
        self.y=y
        print('instance method')
        print(self.y)

    @classmethod
    def class_method(cls):
        print('class method')


    @staticmethod
    def staticmethod():
        print('static method')
        print(Typesofmethod.x)


t=Typesofmethod()
t.instance(100)
Typesofmethod.class_method()
Typesofmethod.staticmethod()"""
class Assignment:
    x=10
    y=20
    def method_one(self,x):
        self.z=30
        print(Assignment.x)
        print(Assignment.y)
        print(x)
        print(self.z)
    @classmethod
    def method_two(cls,y):
        print(Assignment.x)
        print(Assignment.y)
        print(y)
ass=Assignment()
ass.method_one(100)
ass.method_two(22)



