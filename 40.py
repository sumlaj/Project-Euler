import time
tStart = time.time()

from decimal import *
a=''
for i in range(1,30000):
    a=a+str(i)

print int(a[0])*int(a[9])*int(a[99])*int(a[999])*int(a[9999])*int(a[99999])

print "Run Time = " + str(time.time() - tStart)
