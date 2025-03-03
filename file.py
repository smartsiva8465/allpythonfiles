f=open('demo.txt','w')
f.write('welcome to python language\n')
f.write('we are knowing about file topic\n')
f.close()
f=open('demo.txt','a')
f.write('hello python\n')
f.write('welcome back\n')
f.close()
f=open('demo.txt','r')
#readlines
res=f.readlines()
print(res)
f.close()
#for loop prints line by line
f=open('demo.txt','r')
for i in f:
    print(i)
#exceptions in file
try:
   file=open('calculator.txt','r')
   l1=file.readlines()
   print(l1[6])
   file.close()
except FileNotFoundError:
    print('no such file...')
except IndexError:
    print('trying to print')



