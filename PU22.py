import time
tStart = time.time()
for i,v in enumerate(sorted(eval(open('names.txt').readline()))):
    sm+=(i+1)*sum([ord(k)-64 for k in list(v)])
print sm
print "Run Time = " + str(time.time() - tStart)
