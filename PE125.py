import time
tStart = time.time()
from include import is_pal
 
limit = 10**8
sqrt_limit = int(limit**.5)
pal = set()
 
for i in xrange(1, sqrt_limit):
  sos = i*i
  for j in xrange(i+1, sqrt_limit):
    sos += j*j
    if sos>=limit: break
    if is_pal(sos): pal.add(sos)
 
print sum(pal), len(pal)

print "Run Time = " + str(time.time() - tStart)
