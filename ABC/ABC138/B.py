N = int(input())
A_list = list(map(int,input().split()))

# A1...Anの積を求める
p = 1
for a in A_list :
    p *= a

bunbo = 0
for a in A_list :
    bunbo += p/(1.0*a)

print(p/bunbo)
