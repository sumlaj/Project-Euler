#sieve of eratosthanese  http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
import time
tStart = time.time()
sieve = [True] * 50
sieve[0] = sieve[1] = False

def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    mark(sieve, x)
for n, p in enumerate(sieve):
    if p:
        print n
def dig_list(n):
    digits = []
    for i in xrange(1,len(str(n))):
        digits+=[str(n)[0:i],str(n)[i:len(str(n))]]
    return digits
l=[]
for n, p in enumerate(sieve):
    if p and n!=2 and n!=3 and n!=5 and n!=7:
        isprime=True
        for i in dig_list(n):
            if not sieve[int(i)]:
                isprime = False
                break
        if isprime:
            l.append(n)
#print dig_list(3797)

print l,len(l),sum(l)
print "Run Time = " + str(time.time() - tStart)
