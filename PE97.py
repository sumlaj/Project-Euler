import time
tStart = time.time()
#7830457
print str(28433*pow(2,7830457,10**10)+1)[-10:]
print "Run Time = " + str(time.time() - tStart)
