import time
tStart = time.time()
from fractions import gcd
z=0
ar=[]
for i in range(4,6):
    l=[]
    for d in range(1,i):
        if gcd(i,d) ==1:
             l.append(d)
    r = i/float(len(l))
    if r>z:
        z=r
        t=(i,z)
print t
print "Run Time = " + str(time.time() - tStart)

# answer is 510510 deduced by thinking, after 6 it's 30 = 6*5 then 210 = 30 * 7,then * 11 then * 13 that is prime numbers
