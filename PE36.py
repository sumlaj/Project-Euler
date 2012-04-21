import time
tStart = time.time()
s=0
for i in range(1,1000001):
    if str(i) == str(i)[::-1]:
        if bin(i)[2:] == bin(i)[:1:-1]:
            s=s+i
print s

print "Run Time = " + str(time.time() - tStart)
