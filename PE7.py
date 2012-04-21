import time
tStart = time.time()
c=6
l=[2, 3, 5, 7, 11,13]
from math import ceil

for i in range(17,10000000,2):
    p=1
    for d in range(3,int(ceil(i**0.5))+1,2):
        p = p*ceil((i%d))
        #if i==25:
            #print d,p
    if p!=0:
        #print i
        #pass
        
        #if i%d == 0:
            #print i
            #continue
        c=c+1
        #print i
    if c==10001:
        print i
        print "Run Time = " + str(time.time() - tStart)
        import sys
        sys.exit(1)

#answer 104743
