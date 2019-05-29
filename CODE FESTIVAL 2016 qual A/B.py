N = int(input())
li = [int(i) for i in input().split()]

c = 0
for i in range(1,N+1) :
    # iを基準に行って帰ってこれればOK
    if (i == li[li[i-1]-1]) :
        c += 1

print(c//2)