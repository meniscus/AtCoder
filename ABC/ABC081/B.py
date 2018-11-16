N = int(input())
l = [int(i) for i in input().split() ]

counter = 0
f = False
while True :
	for i in range(len(l)) :
		if (l[i] % 2 == 0) :
			l[i] = int(l[i] / 2)
		else :
			f = True
			break;
	
	if (f == True) :
		break
	
	counter += 1

print(counter)