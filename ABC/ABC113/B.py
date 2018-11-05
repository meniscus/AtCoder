def get_temp(t,h) :
	return T - h * 0.006

N = int(input())

read_line = input().split()
T = int(read_line[0])
A = int(read_line[1])

height_list = [int(s) for s in input().split()]

diff = 99999
diff_index = 0

for i in range(len(height_list)) :
	temp = get_temp(T,height_list[i])
	
	if (abs(temp - A) < diff) :
		diff = abs(temp -A)
		diff_index = i
	


print (diff_index+1)
