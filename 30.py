import time
tStart = time.time()

s=0
for i in range(2,200000):
    d=0
    for n in str(i):
        d=d+int(n)**5
    if d==i:
        s=s+i
print s

print "Run Time = " + str(time.time() - tStart)
