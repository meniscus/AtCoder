N,K = input().split()
N = int(N)
K = int(K)

trees = []
for i in range(N) :
	trees.append(int(input()))

trees.sort()
min_diff = 99999999999
for i in range(N-K+1) :
	max_v = trees[i+K-1]
	min_v = trees[i]
	diff = max_v - min_v
	if (min_diff > diff) :
		min_diff = diff
	if (min_diff == 0) :
		break



print(min_diff)