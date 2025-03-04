def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
print(fact(5))

s="1234"
p=int(s)
print(p)
def areaofrect(l,w):
    return l*w
print(areaofrect(5,3))
d1={
    'name':'siva',
    'age':22
}
d2={
    'city':'knl',
    'pin':'87654'
}
d3={**d1,**d2}
print(d3)


l1=[1,3,5,7]
l2=[2,4,3,1]
l3=list(set(l1)&set(l2))
print(l3)
l1=[1,3,5,7,1]
l2=list(set(l1))
print(l2)
def palindrome(s):
    return s==s[::-1]
print(palindrome('sos'))

def count_uppercase(s):
    return sum( 1 for char in s if char.isupper())

print(count_uppercase("NxtWave"))
def intersection(set1, set2):
    return set1 & set2

print(intersection({1, 2, 3}, {2, 3, 4}))
print('siva')



