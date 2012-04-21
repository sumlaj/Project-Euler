import time
tStart = time.time()
for i in xrange(1000000070,1400000000,100):
    s=str(i**2)
    #if s[0]=='1' and s[2]=='2' and s[4]=='3' and s[6]=='4' and s[8]=='5' and s[10]=='6' and s[12]=='7' and s[14]=='8':
        #print i,i**2
        #break
    if s[0]=='1' and s[14]=='8' and s[2]=='2' and s[4]=='3' and s[6]=='4' and s[8]=='5' and s[10]=='6' and s[12]=='7':
        print i,i**2
        break
    
print "Run Time = " + str(time.time() - tStart)
    
