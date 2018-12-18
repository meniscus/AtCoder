N = int(input())
X = [int(i) for i in input().split()]
X2 = sorted(X)
mapper = {}

for i in range(N//2) :
    if (X2[i] in mapper) :
        continue
    mapper[X2[i]] = X2[len(X2)//2]

for i in range(N//2,N) :
    if (X2[i] in mapper) :
        continue
    mapper[X2[i]] = X2[(len(X2)//2) - 1]

for x in X :
    print(mapper[x])