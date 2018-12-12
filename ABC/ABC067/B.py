N,K = [int(i) for i in input().split()]
sticks = [int(i) for i in input().split()]
sticks.sort(reverse=True)
sum = 0
for i in range(K) :
    sum += sticks[i]

print(sum)