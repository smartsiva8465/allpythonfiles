#one method
import first
first.welcome()

#choosen multiple methods
from first import second,third
second()
third()
#ambigity
from first import *
from second import*
second()
#another approach to call both
import first as a
import second as b
a.second()
b.second()
#import random type
import random
print(random.randint(1,20)) # Random integer between 1 and 100 (inclusive)
print(random.random()) # Random float between 0 and 1
print(random.uniform(10,20))# Random float between 10 and 20
print(random.randrange(0,100,2)) # Random even number from 0 to 100
list=['apple','banana','grapes']
print(random.choice(list))# Randomly selects one item
print(random.choices(list,k=2))# Randomly selects 2 items (with replacement)
print(random.sample(list,2)) # Randomly selects 2 unique items (without replacement)
num=[1,2,3,4,5,6]
random.shuffle(num)
print(num)
print(random.gauss(0,1))
print(random.expovariate(1.5))
#package module






