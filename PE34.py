import time
tStart = time.time()
from math import factorial as f

for i in range(10,1000000):
    s=0
    for n in str(i):
        s=s+f(int(n))
    if s==i:
        print i
print "Run Time = " + str(time.time() - tStart)
