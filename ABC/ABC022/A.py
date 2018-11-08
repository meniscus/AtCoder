import math
# あ
read_line = input().split()
days = int(read_line[0])
under_limit = int(read_line[1])
upper_limit = int(read_line[2])

best_body_days = 0
weight = 0
for i in range(days) :
	weight += int(input())
	if (under_limit <= weight and weight <= upper_limit) :
		best_body_days += 1
	

print(best_body_days)