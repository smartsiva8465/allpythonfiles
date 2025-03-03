li=[2,4,5,6,7]
#reverse
for i in range(len(li)-1,-1,-1):
    print(li[i],end=",")
print('\n')
 #sum of elements
sum=0
for i in li:
    sum=sum+i
print(sum)
#sum of even elements
sum=0
for i in li:
    if i %2==0:
        sum=sum+i
print('sum of even elements is :',sum)
#odd elements
sum=0
for i in li:
    if i %2==1:
        sum=sum+i
print('sum of odd elements is :',sum)
#even indices
sum=0
for i in range(len(li)):
    if i % 2==0:
        sum=sum+li[i]
print('sum of even indices:',sum)
#odd indices
sum=0
for i in range(len(li)):
    if i % 2==1:
        sum=sum+li[i]
print('sum of odd indices:',sum)
#reverse
list=[15,25,35,45]
for i in range(len(list)-1,-1,-1):
  print(list[i],end=" ")
print('\n')
  #
nums=[10,20,30,40,50,60,70,80,90,100]
for i in range(0,9,2):
    if i % 2 == 0:
        print(nums[i],end=" ")
print('\n')
#ass3
mylist=[10,20,30,40,50]
sum=0
for i in mylist:
    sum=sum+i
print(sum)
print('\n')
#biggest
l2=[10,200,30,400,50]
biggest=0
for i in l2:
    if i>biggest:
        biggest=i
print(biggest)
#smallest
smallest=l2[0]

for i in l2:
    if i< smallest:
        smallest=i
print(smallest)

































