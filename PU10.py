'''PE 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import time
tStart = time.time()
c = 6
l = [2, 3, 5, 7, 11, 13] #initialized an array of 1st 6 prime numbers
from math import ceil

for i in xrange(17, 2000, 2): #checking odd numbers from 17
    p = 1
    for d in range(3, int(ceil(i**0.5))+1, 2):
        #upto ceil of square root of current number
        #checking remainder
        p = p*ceil((i%d)) 
    if p != 0:
        #no remainder contain zero which means 
        #number is not completely divisible and so it's prime
        l.append(i)
print sum(l)
    
print "Run Time = " + str(time.time() - tStart)        
