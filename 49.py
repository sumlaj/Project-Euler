#sieve of eratosthanese  http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
import time
tStart = time.time()
sieve = [True] * 10000
from itertools import permutations
sieve[0] = sieve[1] = False

def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    mark(sieve, x)
l=[]
for i in xrange(1000,10000):
    if sieve[i]:
        l.append(i)
for i in l:
    if i+3330 in l and i+6660 in l:
        print i,i+3330,i+6660

print "Run Time = " + str(time.time() - tStart)
