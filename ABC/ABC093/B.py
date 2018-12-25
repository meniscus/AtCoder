A,B,K = [int(i) for i in input().split()]

counter = 1
ans_list = []
for i in range(A,B+1) :
	ans_list.append(i)
	counter += 1
	if (counter > K) :
		break

counter = 1
for i in range(B,A,-1) :
	ans_list.append(i)
	counter += 1
	if (counter > K) :
		break

ans_list = list(set(ans_list))
ans_list.sort()
for i in ans_list :
	print(i)


