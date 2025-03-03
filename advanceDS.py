x=['hi','python','we','write','python','we','say','hi','python']
y={}
for i in x:
    if i in y.keys():

        y[i]=y[i]+1
    else:
        y[i]=1
print(y)
print('\n')
#requirement 2
li=[('a', 10), ('b', 20), ('c', 30), ('d', 40)]
y=[i for _,i in li]
#requirement 3
w=['a','b','c','d']
x=[10,20,30,40]
z={w[i]:x[i] for i in range(len(w))}#dictionary
a=[(w[i],x[i]) for i in range(len(w))]#tuples in list
print(*y)
print(z)
print(a)
#requirement 5
b=[('hi','noun'),('good','adj'),('run','verb'),('bad','adj'),('good','adj')]
c=[i[0] for i in b if i[1]=='adj']
print(c)
good_count=0
bad_count=0
for i in c:
    if i=='good':
        good_count=good_count+1
    else:
        bad_count=bad_count+1
if good_count > bad_count:
    print('sentiment is positive')
elif good_count < bad_count:
    print('sentiment is negative')
else:
    print('sentiment is neutral')
