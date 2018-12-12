N = int(input())
in_list = [int(i) for i in input().split()]

m = 0
for a in in_list :
    m += a - 1

print(m)
	