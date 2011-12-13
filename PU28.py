import time
tStart = time.time()
l=[1]
n=0
for i in range(2001):
    l.append(l[-1]+n)
    if i%4 == 0:
        n=n+2
print sum(l)
print "Run Time = " + str(time.time() - tStart)


