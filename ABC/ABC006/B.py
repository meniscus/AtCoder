N = int(input())

tribonacci = [0,0,1]

if N <= 2 :
	print(0)
elif N == 3 :
	print(1)
else :
	for i in range(3,N) :
		n = tribonacci[0] + tribonacci[1] + tribonacci[2]
		tribonacci.append(n)
		tribonacci.pop(0)

	res = tribonacci[-1]
	print(res % 10007)
