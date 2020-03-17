import math
N,K = map(int,input().split())

if (math.ceil(N/2) >= K) :
    print("YES")
else :
    print("NO")