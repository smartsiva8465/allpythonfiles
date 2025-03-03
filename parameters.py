#positional argument
def fun(x,y):
    print('x','=',x)
    print('y', '=',y)
fun(x=10,y=20)
#keyword
def fun(x,y):
    print('x','=',x)
    print('y', '=',y)
fun(y=10,x=20)
#default parameter
def fun(name,age,cource='python'):
    print('name =',name)
    print('age =', age)
    print('cource =',cource)
fun('siva',22,'java')
print('\n')
fun('raj',23)
#arbitery
def fun(*args):
    for i in args:
        print(args)
fun(2)
fun('siva',22)
#
def fun(x,*y,z=100):
    print(x)
    print(y)
    print(z)
fun(10,20,30,40,60)
fun(10,20,30,40)
fun(10,20,30,40,z=108)
#hospital
def fun(name,bg,*disease,email='abc@gmail.com'):
    print(name)
    print(bg)
    print(disease)
    print(email)
fun('siva','b+ve','fever','cold')
fun('raj','a+ve','cough','cold',email='siva@gmail.com')
#2nd

def student(name,*mail,**address):
    print(name)
    print(mail)
    print(address)
student('siva','siva@gmail.com','tej@gmail.com',hno=1,street='bang',pin=518002)



