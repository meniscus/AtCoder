read_line = [int(i) for i in input().split()]
n = read_line[0]
x = read_line[1]

if (n / 2 < x) :
	x = n - x + 1

print(x-1)