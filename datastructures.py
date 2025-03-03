#list methods
li=[1,2,3,4,5]
inserted=int(input('enter a inserted number:'))
pos=int(input('enter a position:'))
li.insert(pos,inserted)
print(li)
element=int(input('enter an element to be delete:'))
if element in li:
    li.remove(element)
print(li)
pos_del=int(input('enter a position:'))
li.pop(pos_del)
print(li)
ele=int(input('enter an element to print position:'))
if ele in li:
    print(li.index(ele))
else:
    print(-1)
#tuple methods
tu=(2,4,5,6,7)
element=int(input('enter an element:'))
if element in tu:
  print( tu.index(element))
#dictionary methods
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
print(dict)
print('\n')
new_name=input('enter n new name:')
dict['name']=new_name
print(dict)
print('\n')
dict.pop('email')
print(dict)
print('\n')
value=input('enter a value to check in dictionary:')
if value in dict.items():
    print('value in dictionary')
else:
    print('not found')
state=input('enter state:')
dict['state']=state
print(dict)
#list comprehention
x=[2,7,3,9,10]
y=[x[i]**2 for i in range(len(x))]# to print [4, 49, 9, 81, 100]
z=[x[i]*2 for i in range(len(x))]#to print [4, 14, 6, 18, 20]
s=[x[i]**2 for i in range(len(x))if i%2==1]#sum of odd indices
p=[i**2 for i in x if i%2==0]#sum of even elements
w=[x[i] for i in range(len(x)) if x[i]%3==0]#multiple of 3
k=[x[i]for i in range(len(x))if i%2==0]#even elements
l=[x[i]for i in range(len(x))if i%2==1]#odd elements
m=[x[i]for i in range(len(x))if i%2==0]#even indices
n=[x[i]for i in range(len(x))if i%2==1]#odd indices
sumofeven=[sum(i for i in x if i %2==0)]#sum of even elments
sumofodd=[sum(i for i in x if i %2!=0)]#sum of odd elments
evenind=[sum(x[i] for i in range(len(x)) if i%2==0)]#sum of even indices
oddind=[sum(x[i] for i in range(len(x)) if i%2!=0)]#sum of odd elements
print(k)
print(l)
print(y)
print(z)
print(s)
print(p)
print(w)
print('even indices:',m)
print('odd indices:',n)
print(sumofeven)
print(sumofodd)
print(evenind)
print(oddind)












