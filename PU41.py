'''PE 41
http://projecteuler.net/problem=41
We shall say that an n-digit number is pandigital if it makes use of 
all the digits 1 to n exactly once. For example, 2143 is 
a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

from math import ceil
def is_prime(n):
    '''checking whether a number is prime 
    '''
    p = 1
    for d in xrange(3, int(ceil(n**0.5))+1, 2):
        #finding product of remainders for divisors upto 
        #ceil plus one of square root of given number
        p = p*ceil((n % d))
        if p == 0:
            return False
    return True
def per(iterable, r=None):
    '''Modified python itertools permutation code so that
    it will return joined generator'''
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    #modified yield tuple(pool[i] for i in indices[:r])
    yield int(''.join(pool[i] for i in indices[:r]))#yielding integer values
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                #modified yield tuple(pool[i] for i in indices[:r])
                yield int(''.join(pool[i] for i in indices[:r]))
                break
        else:
            return
def panprime(m):
    '''return largest m digit pandigital prime'''
    s = '123456789'#initialized 1-9 pandigital as string
    #iterates on a reverse sorted permuted list of pandigital
    for i in sorted(list(per(s[:m])), reverse=True):
        if is_prime(i):#checking if prime 
            return i
def main():
    '''finding largest n-digit pandigital prime
    '''
    import time
    tStart = time.time()
    #making a list of expected digits neglecting 2 digit numbers as the 
    #question itself has given 4 digit number and
    #removing 3,6,8 and 9 digits as they are all divisible by 3
    for j in [7, 5, 4]:
        k = panprime(j)
        if k:
            print k
            break
    print "Run Time = " + str(time.time() - tStart)
    return 0

if __name__ == '__main__':
    main()




