import sys

N = int(sys.stdin.readline())
num = [int(i) for i in sys.stdin.readline().split()]

if(num.count(0)) :
    count = 1
    visit = 1
    for i in range(num.index(0)+1, N) :
        if(visit >= 3) :
            visit = 0
        if(visit == num[i]) :
            count += 1
            visit += 1
    print(count)
else :
    print(0)