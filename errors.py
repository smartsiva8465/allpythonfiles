x='siva prasad'
print(x)
try:

   print(x[11])
except Exception as e:
    print(e)
try:
    print(x(19))

except Exception as f:
    print(f)
print(x[1:8])
try:
    x=int(input('please enter a number'))
    print(x)
except ValueError:
       print('enter a valid number...')
except NameError:
      print('x is invalid')
try:
   y=[10,20,30]
   print(y[0])
   print(y[1])
   print(y[2])
   print(y[3])
except IndexError:
    print('you are accessing wrong position')

try:
    print(x)
except NameError:
    print('x is not defined')
except ValueError:
    print('handled')
finally:
    print('something is wrong')


