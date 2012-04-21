import time
tStart = time.time()
e=set()
f=set()
g=set()
for a in range(1,100000):
    e.add(a*(a+1)/2)
for b in range(1,100000):
    f.add(b*(3*b-1)/2)
for c in range(1,100000):
    g.add(c*(2*c-1))
print e.intersection(f,g)

print "Run Time = " + str(time.time() - tStart)
