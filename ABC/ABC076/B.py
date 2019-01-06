N = int(input())
K = int(input())

current = 1
for i in range(N) :
	if (current < K) :
		current = current * 2
	else :
		current = current + K

print(current)