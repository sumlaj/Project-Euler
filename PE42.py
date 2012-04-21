import time
tStart = time.time()
t=[]
for i in xrange(1,21):
    t.append(i*(i+1)/2)
sm = []
for i,v in enumerate(eval(open('words.txt').readline())):
    sm.append(sum([ord(k)-64 for k in list(v)]))
count = 0
for i in sm:
    if i in t:
        count+=1
print count
print "Run Time = " + str(time.time() - tStart)
