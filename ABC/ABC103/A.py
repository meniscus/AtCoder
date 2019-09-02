A1,A2,A3 = map(int,input().split())

min_cost = abs(A1-A2)
if (min_cost < abs(A2-A3)) :
    min_cost = abs(A2-A3)

if (min_cost < abs(A1-A3)) :
    min_cost = abs(A1-A3)

print(min_cost)