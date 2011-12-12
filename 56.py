import time
tStart = time.time()
s=0
d=0
for i in range(1,100):
    for j in range(1,100):
        n = i**j
        for m in str(n):
            s = s+int(m)
        if s>d:
            d=s
        s=0
print d
print "Run Time = " + str(time.time() - tStart)
# kewl method
tStart = time.time()
print max( [ sum( [ int( i ) for i in str( a ** b ) ] ) for a in xrange( 90, 100 ) for b in xrange( 90, 100 ) ] )
print "Run Time = " + str(time.time() - tStart)
