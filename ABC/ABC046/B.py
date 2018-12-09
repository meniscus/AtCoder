N, K = [int(i) for i in input().split()]

patterns = K
for i in range(N-1) :
	patterns *= (K-1)

print(patterns)
