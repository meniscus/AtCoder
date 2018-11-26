N = int(input())
S = list(str(N))

sum = 0
for s in S :
	sum += int(s)

if (N % sum == 0) :
	print("Yes")
else :
	print("No")