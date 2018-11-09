# あ
read_line = [int(i) for i in input().split()]
a = read_line[0]
b = read_line[1]
c = read_line[2]
k = read_line[3]

read_line = [int(i) for i in input().split()]
s = read_line[0]
t = read_line[1]


price = a * s + b * t

if (s+t >= k) : 
	price -= (s+t) * c

print(price)