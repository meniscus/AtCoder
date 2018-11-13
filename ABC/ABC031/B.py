def get_must_exercise_time(L,H,t) :
	if (H < t) :
		return -1
	elif (L < t) :
		return 0
	else :
		return L-t

read_line = [int(i) for i in input().split()]
L = read_line[0]
H = read_line[1]

N = int(input())

exercise_time = []
for i in range(N) :
	exercise_time.append(int(input()))

for i in range(N) :
	print(get_must_exercise_time(L,H,exercise_time[i]))


