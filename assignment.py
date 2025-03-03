n1= int(input('enter the first value:'))
n2=int(input('enter the second value:'))
n3= int(input('enter the third value:'))
biggest=max(n1,n2,n3)
print('the biggest number is:',biggest)
#vowel or not
char=input('enter the character:')
if char in ( 'a','e','i','o,','u'):
    print('given char is vowel')
else:
    print('given char is a consonent')
#vote eligibility
age=int(input('enter the age:'))
nationlity=input('enter the nation:')
if nationlity == 'INDIA' and age >= 18:
    print('eligible for voting')
else:
    print('not eligible for voting')
#biggest number
n1=int(input('enter the first number:'))
n2=int(input('enter the second number:'))
n3=int(input('enter the third number:'))
if n1>n2 or n1>n3:
    print(n1,'is bigger')
elif n2>n3:
    print(n2,'n2 is bigger')
else:
    print(n3,'is bigger')
#leap year
year=int(input('enter the year:'))
if year % 4 == 0:
    print(year,'is leap year')
elif year % 100 != 0:
    print(year,'is leap year')
elif year%400==0:
    print(year,'is leap year')
else:
    print(year,'is not a leap year')
#percendtage and grades
marks=int(input('enter the marks:'))
total_marks=int(input('enter the total_marks:'))
percentage=(marks/total_marks*100)
if percentage >= 90 :
    print('GRADE:A')
elif 80<=percentage<90:
    print('GRADE:B')
elif  70<=percentage<80:
    print('GRADE:C')
elif 35< percentage<50:
    print('FAIl')
else:
    print('OOPS better luck next time')
#while loop
x=1
sum=0
while x<=10:
    sum=sum+x
    x=x+1
    print(sum)
x=2
while x<=512:
    print(x)
    x=x**3
x=1
while x<=100:
    print(x,end=' ')
    x=x+2
#
list=[2,4,6,8,10]
sum=0
x=0
while x<=len(list)-1:
    sum=sum+list[x]
    x=x+1
    print(sum,end=' ')
    print('\n')
#print prefer indices
list=[10,22,11,35,5]
index=[2,3,4]
sum=0
x=0
while x<len(index):
    sum=sum+list[index[x]]
    x=x+1
    print(sum,end=' ')
#even and odd sum elements
list=[10,22,11,35,5]
even_sum=0
odd_sum=0
i=0
while i < len(list):
    if list[i] % 2==0:
        even_sum= even_sum+list[i]
    else:
        odd_sum=odd_sum+list[i]
    i=i+1
print("sum of even:",even_sum)
print("sum of odd:",odd_sum)
#even elements
li=[2,4,5,6,7]
for i in li:
    if i %2 == 0:
        print(i,end=' ')
#print even index
li=[2,4,5,6,7]
for i in range(0,5):
    if i % 2==0:
        print(li[i],end=' ')
#dictionary loops
dict={     }
print('dictionary:',dict)
dict={

    'name':input('enter the name:'),
    'email':input('enter the email:'),
    'mobile':int(input('enter the number:')),
    'city ':input('enter the city:'),
    'pin':input('enter the pin:')
}
for key,value in dict.items():
    print(key,'=',value)
#store dict
print(dict)
#function,return,even  or odd
integer=int(input('enter number:'))
def fun(integer):
     if integer % 2==0:
         return 'even'
     else:
        return 'odd'
res=fun(integer)
print(integer,'is',res)
#string reverse
string='siva'
def fun(string):
  return string[::-1]
print(fun(string))
#word count
st='good evening siva prasad'
wordcount=1
for i in st:
    if i ==' ':
        wordcount=wordcount+1
print(wordcount)
#space count
spacecount=0
for i in st:
    if i ==' ':
        spacecount=spacecount+1
print(spacecount)
#
num=input('enter the number :')
def fun(num):
    return num[::-1]
print(fun(num))
#reverse numbers
num=int(input('enter the number :'))
rev=0
while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print(rev)
#image
from PIL import Image
img=Image.open('IMG-20241018-WA0026.jpg')
img.show()
#vowel with in  string
char=input('enter the character:')
st='aeiou'
for i in st:
    if char in st:
        res=f'{char} is a vowel'
    else:
        res=f'{char} is not a vowel'
print(res)
#vowel with in list
char=input('enter the character:')
list=['a','e','i','o','u']
for i in list:
    if char in list:
        res=f'{char} is a vowel'
    else:
        res=f'{char} is not a vowel'
print(res)
#palindrome using slicing
def palindrome(s):
    return s==s[::-1]
st=input('enter the text:')
if palindrome  (st):
    print('is palindrome')
else:
    print('not a palindrome')
# palindrome using reverse
def palindrome(s):
    return s== ''.join(reversed(s))
st=input('enter the text:')
if palindrome  (st):
    print('is palindrome')
else:
    print('not a palindrome')
 #palindrome
s='miss'
print(s[::-1])
print(s==s[::-1])

