import time
tStart = time.time()
a=set()
for i in xrange(100,5000):
    for j in xrange(2,100):
        p = i*j
        if len(str(p)) == 4:
            s = list(str(i))+list(str(j))+list(str(p))
            if set(s) == set(['1', '3', '2', '5', '4', '7', '6', '9', '8']):
                a.add(p)
               
print sum(a)
print "Run Time = " + str(time.time() - tStart)
