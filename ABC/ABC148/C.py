import fractions as frac

A,B = map(int,input().split())
print(A * B // frac.gcd(A,B))