import time
tStart = time.time()
from math import factorial
c=0
for i in range(1,101):
    for j in range(1,i+1):
        if factorial(i)/(factorial(j)*factorial(i-j)) > 1000000:
            c=c+1
print c
print "Run Time = " + str(time.time() - tStart)
