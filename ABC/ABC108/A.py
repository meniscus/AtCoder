# あ
K = int(input())

odd = []
even = []
for i in range(1,K+1) :
	if (i % 2 == 1) :
		odd.append(i)
	else :
		even.append(i)

print(len(odd) * len(even))
