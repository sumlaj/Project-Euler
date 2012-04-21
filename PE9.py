import time
tStart = time.time()
for a in range(1,1001):
    for b in range(1,1001):
        #for c in range(1,101):
            #if a+b+c == 1000 and a**2 + b**2 == c**2:
                #print a,b,c
        if 1000*(a+b) - a*b == 500000:
            print a,b

print "Run Time = " + str(time.time() - tStart)
