import time
tStart = time.time()
import itertools
print list(itertools.permutations(range(10)))[999999]
print "Run Time = " + str(time.time() - tStart)
