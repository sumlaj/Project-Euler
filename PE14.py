import time
tStart = time.time()
cp=0
t=0
a=range(1,1000000)
for i in a:
    tmp=i
    c=0
    while i!=1:
        if i%2 == 0:
            #if i in a:
             #   a.remove(i)
            #a.remove(i)
            i = i/2
            c = c+1
        else:
            #if i in a:
             #   a.remove(i)
            i = 3*i +1
            c = c+1
    if c>=cp:
        t=tmp
        cp=c
print t,cp
print "Run Time = " + str(time.time() - tStart)

#837799
