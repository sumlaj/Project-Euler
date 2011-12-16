import time
tStart = time.time()
f = open('names.txt')
s = f.readline()
s = s.split('","')
s[0] = s[0][1:]
s[-1] = s[-1][:-1]
sm = 0
for i,v in enumerate(sorted(s)):
    sm+=(i+1)*sum([ord(k)-64 for k in list(v)])
print sm
print "Run Time = " + str(time.time() - tStart)
