N = int(input())
nice_yaku = []
for i in range(1,N+1) :
	if i % 2 == 0 :
		# 偶数は除外する
		continue

	yaku = []
	for j in range(1,i+1) :
		if i % j == 0 :
			yaku.append(j)

	if len(yaku) == 8 :
		nice_yaku.append(i)

print(len(nice_yaku))