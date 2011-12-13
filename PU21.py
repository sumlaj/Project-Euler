import time
tStart = time.time()
d={}

for i in range(2,10000):
    l=[]
    for j in range(1,i):
       if i%j == 0:
           l.append(j)
    d[i]=sum(l)
s=set()
for k,v in sorted(d.items()):
    try:
        if d[v] in d and d[v]!=v and d[v]==k:
             s.add(k)
             s.add(d[v])
    except KeyError:
        pass
print sum(list(s))

    

print "Run Time = " + str(time.time() - tStart)
