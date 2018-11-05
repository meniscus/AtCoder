rate = 0

read_line = input().split()
can_watch_count = int(read_line[1])

read_line = input().split()

teacher_rate_list = []
for i in range(len(read_line)) :
	teacher_rate_list.append(int(read_line[i]))

teacher_rate_list.sort()
teacher_rate_list.reverse()
watch_list = teacher_rate_list[0:can_watch_count]
watch_list.sort()

for i in range(len(watch_list)) :
	rate += pow(2,i) * watch_list[i]

rate = rate / pow(2, len(watch_list))

print(rate)