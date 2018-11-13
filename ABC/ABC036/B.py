N = int(input())
rows = []
for i in range(N) :
	rows.append(list(input()))

rot = []
out_list = []
for n in range(N) :
	for m in range(N) :
		rot.append(rows[N-m-1][n])
	out_list.append(''.join(rot))
	rot = []

for n in range(len(out_list)) :
	print(out_list[n])