in_rows = 4
in_list = []
for i in range(in_rows) :
	in_list.append(input().split())

for i in range(in_rows)[::-1] :
	print(" ".join(in_list[i][::-1]))

