# 全部2枚にするのはNG?
flower_count = int(input())
valid_leaves = [1,3,7,9]

read_line = input().split()
flower_list = []
for s in read_line :
	flower_list.append(int(s))

remove_leaves = 0
for current_leaves in flower_list :
	for leaves in valid_leaves[::-1] :
		if (current_leaves >= leaves) :
			remove_leaves += current_leaves - leaves
			break;

print(remove_leaves)