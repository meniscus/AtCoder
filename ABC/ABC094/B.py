N,M,X = [int(i) for i in input().split()]
gates = [int(i) for i in input().split()]

fare = 0

# 減少方向
for i in range(X) :
    if (i in gates) :
        fare += 1

min_fare = fare
fare = 0
for i in range(X,N+1) :
    if (i in gates) :
        fare += 1

if (min_fare > fare) :
    min_fare = fare

print(min_fare)