import time
tStart = time.time()
def fsum(triangle):
    while len(triangle) > 1:
        tri(triangle)
    return triangle[0][0]
def tri(red):
    lrow = red[-1]
    for index in xrange(len(red) - 1):
        red[-2][index] += max(lrow[index:index + 2])
    del red[-1]

def main():
    a = [map(int, x) for x in [line.split(' ') for line in list(open('triangle.txt'))]]
    print fsum(a)


if __name__ == '__main__':
    main()


print "Run Time = " + str(time.time() - tStart)
