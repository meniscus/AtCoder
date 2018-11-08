import math
# あ
N = int(input())
ret = []
if (N % 2 == 0) :
	for i in range(int(N / 2)) :
		ret.append(2)
else : 
	ret.append(1)
	for i in range(int((N - 1) / 2)) :
		ret.append(2)

print(len(ret))
[print(i) for i in ret]