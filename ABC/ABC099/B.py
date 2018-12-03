a,b = [int(i) for i in input().split()]

n = b-a

right_height = 0
for i in range(1,n+1) :
	right_height += i

print(right_height - b)