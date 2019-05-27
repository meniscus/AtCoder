N,M = [int(i) for i in input().split()]

Lmin = 0
Rmax = N
for i in range(M) :
    L,R = [int(i) for i in input().split()]
    if (Lmin < L) :
        Lmin = L
    
    if (Rmax > R) :
        Rmax = R

if (Rmax-Lmin >= 0) :
    print(Rmax-Lmin+1)
else :
    print(0)
