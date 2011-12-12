import time
tStart = time.time()
c=6
l=[2, 3, 5, 7, 11,13]
from math import ceil

for i in range(17,2000,2):
    p=1
    for d in range(3,int(ceil(i**0.5))+1,2):
        p = p*ceil((i%d))
    if p!=0:
        l.append(i)
print sum(l)
    
print "Run Time = " + str(time.time() - tStart)        
