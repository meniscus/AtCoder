N = int(input())
cost = 0

for i in range(N) :
    a,b = [int(i) for i in input().split()]
    cost += b * a

print(int(cost * 1.05))
