S = input()

diff = 999
for i in range(0,len(S) - 2) :
	n = int(S[i:i+3])
	if (abs(753 - n) < diff) :
		diff = abs(753 - n)

print(diff)

