'''PE 12
http://projecteuler.net/problem=12
'''
def fact(n):
    l = []
    maxi = int(n**0.5)+1
    for i in range(1, maxi):
        if n % i == 0:
            l = l+[i, n/i]
    return len(l)

def main():
    import time
    tStart = time.time()
    d = 2
    while True:
        num = (d*(d+1))/2
        if fact(num) > 500:
            break
        d += 1
    print num
    print "Run Time = " + str(time.time() - tStart)
    return 0

if __name__ == '__main__':
    main()
