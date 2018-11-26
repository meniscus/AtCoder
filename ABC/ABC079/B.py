N = int(input())

a,b,c = 2,1,3

for i in range(N) :
	a,b,c = b,c,b+c

print(a)