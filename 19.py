import time
tStart = time.time()
import calendar
c=0
for y in range(1901,2001):
    for m in range(1,13):
        if calendar.weekday(y,m,1)==6:
            c=c+1
print c



print "Run Time = " + str(time.time() - tStart)
