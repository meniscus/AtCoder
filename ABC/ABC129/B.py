N = int(input())
W = [int(i) for i in input().split()]

S1 = W[0]
S2 = sum(W) - W[0]
diff = abs(S1-S2)

for i in range(1,N) :
    S1 += W[i]
    S2 -= W[i]
    d = abs(S1-S2)
    if (d < diff) :
        diff = d

print(diff)
