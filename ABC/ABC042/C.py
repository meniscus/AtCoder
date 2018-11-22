N,K = [int(i) for i in input().split()]
hate_numbers = [i for i in input().split()]


while True:
	is_okay = True
	for n in hate_numbers :
		if (str(N).find(n) == -1) :
			continue
		is_okay = False
		break
	
	if (is_okay == True) :
		print(N)
		break
	else :
		N += 1

