import time
tStart = time.time()
s=set()
for a in range(2,101):
    for b in range(2,101):
        s.add(a**b)
print len(s)
print "Run Time = " + str(time.time() - tStart)
