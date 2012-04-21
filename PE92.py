def fn(n):
    m=n
    s=0
    for i in str(n):
        s = s+int(i)**2
    if s==89 or s==85 or s==42 or s==20 or s==4 or s==16 or s==37 or s==58:
        return False
    elif s==1 or s==44 or s==32 or s==13 or s==10 or s==100 or s==1000 or s==10000:
        return True
    else:
        return fn(s)

def main():
    import time
    tStart = time.time()
    c=0
    l89=[]
    l1=[]
    for i in range(1,10000000):
        if fn(i):
            c=c+1
    print c
    print "Run Time = " + str(time.time() - tStart)
    return 0

if __name__ == '__main__':
	main()

            
#answer 8581146  # 1's 1418853
