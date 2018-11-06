# あ
read_line = input().split()

m = int(read_line[0])
d = int(read_line[1])

if (m % d == 0) :
	print("YES")
else :
	print("NO")