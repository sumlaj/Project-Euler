import time
tStart = time.time()

from decimal import *
S=[1,2,5,10,20,50,100,200]

def count( n, m ):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m < 0 and n >= 1:
        return 0
 
    return count( n, m - 1 ) + count( n - S[m], m )

def main():
	print count(200,7)
	return 0

if __name__ == '__main__':
	main()

print "Run Time = " + str(time.time() - tStart)
