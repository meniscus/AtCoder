l = [int(i) for i in input().split()]
N,Q = l[0],l[1]

arr = [0] * N
action_list = []
for i in range(Q) :
	read_line = input().split()
	from_index = int(read_line[0]) - 1
	to_index = int(read_line[1]) - 1
	rewrite_val = int(read_line[2])
	
	for j in range(from_index, to_index+1) :
		arr[j] = rewrite_val

for i in range(len(arr)) :
	print(arr[i])


