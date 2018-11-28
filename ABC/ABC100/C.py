N = int(input())
in_str = [int(i) for i in input().split()]

count = 0
for i in range(N) :
	while True :
		if (in_str[i] % 2 == 0) :
			in_str[i] = in_str[i] / 2
			count += 1
			continue
		break

print(count)