#sum of two number
method=lambda n1,n2 : n1+n2
x=method(10,20)
print(x)
#even or odd
fun=lambda num:'even' if num % 2==0 else 'odd'
res=fun(11)
print(res)
#greatest of two numbers
greater=lambda num1,num2:f'{num1} is greater' if num1>num2 else f'{num2} is greater'
res=greater(20,30)
print(res)
#vowel or not

vowel=lambda char:f'{char} is a vowel' if char  in('a','e','i','o','u','A','E','I','O','U')else f'{char} is not vowel'
res=vowel('A')
print(res)
reverse=lambda string:string[::-1]
res=reverse('siva')
print(res)
#split
import re
st= 'good morning siva prasad'
res=re.split(' ',st)
x=['good', 'morning', 'siva', 'prasad']
y=' '.join(x)
a=re.match('good',st)#matching or not
b=re.sub('morning','evening',st)#replacing
c=re.findall('siva prasad',st)
print(res)
print(y)
print(a)
print(b)
print(c)
#threads
from threading import Thread
class MyThread(Thread):
    def run(self):
        print('this is our thread')
m1=MyThread()
m1.run()
def f1(fun,x):
    print('welcome')
    fun(x)
    print('bye')
def f2(x):
    print(x*2)
f1(f2,10)
def f1(fun):
    result =fun(10)
    print(result)
def f2(x):
    return x*2
f1(f2)
#filter
x=[10,20,43,23,5]
y=list(map(lambda i:i*2,x))
print(y)
for i in range(1,6):
    print('*'* i)









