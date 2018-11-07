# あ
read_line = input().split()
route_count = int(read_line[0])
permit_time = int(read_line[1])

route_info = {}
min_cost = 9999
for i in range(route_count) :
	read_line = input().split()
	cost = int(read_line[0])
	time = int(read_line[1])
	if (time > permit_time) :
		continue
		
	if (min_cost > cost) :
		min_cost = cost

if (min_cost != 9999) :
	print(min_cost)
else :
	print("TLE")