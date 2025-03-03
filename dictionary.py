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