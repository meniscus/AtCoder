# あ
N = int(input())
in_list = [int(i) for i in input().split()]
out_list = []
for i in range(len(in_list)) :
	n = in_list[i]
	while True :
		if (n % 2 == 0) :
			n = n / 2
		else :
			break
	out_list.append(n)

out_list = list(set(out_list))
print(len(out_list))