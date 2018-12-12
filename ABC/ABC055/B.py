N = int(input())

power = 1
for i in range(1,N+1) :
    power = i * (power % 1000000007)

print(power % 1000000007)
