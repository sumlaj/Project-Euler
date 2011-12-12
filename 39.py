import time
tStart = time.time()
sq=[]
l=[]
for i in xrange(1,500):
    sq.append(i**2)
for j in sq:
    ji=sq.index(j)
    for k in sq[ji:]:
        #ki=sq.index(k)
        if j+k in sq and sq.index(k)+ji>sq.index(j+k) and sq.index(k)+ji+sq.index(j+k)<=1000:
            l+=[j**0.5+k**0.5+(j+k)**0.5]
max=0
maxnum=0
for i in l:
     if l.count(i)>max:
         max = l.count(i)
         maxnum = i
         
print maxnum

print "Run Time = " + str(time.time() - tStart)
