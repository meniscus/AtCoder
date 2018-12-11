read_line = [int(i) for i in input().split()]
N = read_line[0]
T = read_line[1]

time_line = [int(input()) for i in range(N)]

opened_total_time = 0
time_limit = 0

for i in range(len(time_line)) :
	t = time_line[i]
	if (time_limit > t) :
		opened_total_time += t + T - time_limit
	else :
		opened_total_time += T
	
	time_limit = t + T		


print(opened_total_time)