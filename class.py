class student():
    def name(self):
     print('siva')
     y=19
     print(y)
    def cource(self):
        print('python')
class frontend():
    def html(self):
        print('HYPER TEXT MARKUP LANGUAGE')
    def css(self):
        print('cascading style sheets')
s=student()
s.name()
s.cource()
#methods with parameter
class doctor():
    def do_surgery(self,x,y):
        print('x=',x)
        print('y=',y)
d=doctor()
d.do_surgery('siva','prasad')
#assignemt
class student():
    def __init__(self,no,name,sub):
       self.no=no
       self.name=name
       self.sub=sub
    def display(self,no,name,sub):
        print('number =', no)
        print('name=', name)
        print('sub =', sub)
one=student(987654,'siva','python')
one.display(98765,'prasad','full stack')
#lab assignment
class details():
    def __init__(self,no,name,spec):
        self.no=no
        self.name=name
        self.spec=spec
    def doct2(self):
        print(self.no)
        print(self.name)
        print(self.spec)
x=details(32,'boss','pediatric')
x.doct2()
y=details(43,'alis','dentist')
y.doct2()
#
g=40
class Test:
    cv=30
    def __init__(self,lv):
        self.iv=20
        print(lv)
        print(self.iv)
        print(Test.cv)
        print(globals()['g'])
te=Test(1)

#swaping numbers
class Test:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fun(self):
        self.x=self.x +self.y
        self.y = self.x - self.y
        self.x = self.x - self.y

t1=Test(10,20)
print(t1.x)
print(t1.y)
t1.fun()
print(t1.x)
print(t1.y)
class Siva:
    def __init__(self,x):
        self.y=x
    def f1(self):
            print(self.y)

t1=Siva(100)
print(t1.y)












