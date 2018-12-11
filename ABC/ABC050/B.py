N = int(input())
time_list = [int(i) for i in input().split()]
M = int(input())
drinked_time_list = []
for i in range(M) :
    drinked_time_list.append([int(i) for i in input().split()])

base_total_time = sum(time_list)
for dr in drinked_time_list :
    base_time = time_list[dr[0]-1]
    print(base_total_time-base_time+dr[1])



