# あ
N = int(input())

out_str = ""
for i in range(10) :
	if (111 * i < N and N <= 111 * (i + 1)):
		out_str = str(111*(i+1))

print(out_str)