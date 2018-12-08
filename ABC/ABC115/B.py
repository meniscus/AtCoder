N = int(input())
prices = []

sum = 0
for i in range(N) :
	p = int(input())
	prices.append(p)
	sum += p

max_p = max(prices)
sum -= max_p
sum += int(max_p/2)

print(sum)

