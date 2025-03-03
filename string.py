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
#vowel with in  string
char=input('enter the character:')
st='aeiou'
for i in st:
    if char in st:
        res=f'{char} is a vowel'
    else:
        res=f'{char} is not a vowel'
        print(res)
##palindrome using slicing
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
