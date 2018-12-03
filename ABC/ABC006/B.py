N = int(input())

t1,t2,t3 = 0,0,1

if N <= 2 :
	print(0)
elif N == 3 :
	print(1)
else :
	for i in range(3,N) :
		t1,t2,t3 = t2,t3, t1+t2+t3 % 10007

	print(t3)
