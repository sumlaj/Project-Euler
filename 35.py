#sieve of eratosthanese  http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
import time
tStart = time.time()
sieve = [True] * 1000000
sieve[0] = sieve[1] = False

def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    mark(sieve, x)
def circular(n):
    digits = []
    while n > 0:
        digits.append(str(n % 10))
        n = n / 10
    for d in xrange(1, len(digits)):
        yield int(''.join(digits[d:] + digits[0:d]))

count = 0
for n, p in enumerate(sieve):
    if p:
        iscircularprime = 1
        for m in circular(n):
            if not sieve[m]:
                iscircularprime = 0
                break
        if iscircularprime:
            count = count + 1

print count
print "Run Time = " + str(time.time() - tStart)
