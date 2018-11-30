N = int(input())
li = list(str(N))

Sn = 0
for s in li :
	Sn += int(s)

if (N % Sn == 0) :
	print("Yes")
else :
	print("No")