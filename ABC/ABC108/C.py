import itertools as it
N,K = [int(i) for i in input().split()]

candidates = []
even = []
odd = []
for i in range(1,N+1) :
	i = int(i)
	if (i % K == 0) :
		# Kの倍数は候補にする
		even.append(i)
		continue
	
	if (K % 2 == 0 and i % (K/2) == 0) :
		# Kが偶数だったらK/2も候補としてよい
		odd.append(i)
		continue

# a,b,cの組み合わせ(Kが奇数のとき)
count = len(even) * len(even) * len(even)

# a,b,cの組み合わせ(Kが偶数のとき)
# すべての要素がK/2で揃っているケース
if (K % 2 == 0) :
	count += (len(odd) * len(odd) * len(odd))

print(count)