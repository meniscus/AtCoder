read_line = [int(i) for i in input().split()]

A = read_line[0]
D = read_line[1]

print(max([(A+1)*D, A*(D+1)]))
