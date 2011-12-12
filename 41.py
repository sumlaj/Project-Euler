#sieve of eratosthanese  http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

from math import ceil
def is_prime(n):
    p=1
    for d in xrange(3,int(ceil(n**0.5))+1,2):
        p = p*ceil((n%d))
        if p==0:
            return False
    return True
def per(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield int(''.join(pool[i] for i in indices[:r]))
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield int(''.join(pool[i] for i in indices[:r]))
                break
        else:
            return
def main():
    import time
    tStart = time.time()
    s='123456789'
    l=list(per(s[:3]))+list(per(s[:4])) +list(per(s[:5]))+list(per(s[:6]))+list(per(s[:7]))#+list(per(s[:8]))+list(per(s[:9]))
    for i in reversed(sorted(l)):
        if i%2!=0 and is_prime(i):
             print i
             break
    print "Run Time = " + str(time.time() - tStart)
    return 0

if __name__ == '__main__':
	main()




