import time
tStart = time.time()
a,b,t=1,2,0
for i in range(10000):
    if len(str(b)) == 1000:
        print b,i+3
        break
    else:
        t=b
        b=b+a
        a=t
print "Run Time = " + str(time.time() - tStart)
