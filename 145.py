def reversible(n):
    s=str(n)
    if s[-1]=='0':
        return False
    r=s[::-1]
    if s[0]  in '02468' and s[-1] in '02468':
             return False
    if s[0]  in '13579' and s[-1] in '13579':
             return False
    if s==r:
        return False
    d=n+int(r)
    for i in str(d):
         if i in '02468':
             return False
             break
    return True


def main():
    import time
    tStart = time.time()
    c=0
    m={}
    for i in xrange(10**1,10**4):
        if i in m:
            if m[i]:
                c=c+1
                continue
            else: continue
        if reversible(i):
            c=c+1
            m[int(str(i)[::-1])]=True
        else:
            m[int(str(i)[::-1])]=False
    
    print c
    print "Run Time = " + str(time.time() - tStart)
    return 0

if __name__ == '__main__':
    main()
