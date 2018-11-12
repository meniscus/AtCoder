# あ
def get_moved(A, B, d) :
	if (d < A) :
		return A
	elif (d > B) :
		return B
	else :
		return d

read_line = [int(i) for i in input().split()]
N = read_line[0]
A = read_line[1]
B = read_line[2]
location = 0

move_info = []
for i in range(N) :
	read_line = input().split()
	moved = get_moved(A,B, int(read_line[1]))
	
	
	if (read_line[0] == "East") :
		location += moved
	else :
		location -= moved


if (location > 0) :
	print("East " + str(abs(location)))
elif (location < 0) :
	print("West " + str(abs(location)))
else :
	print("0")
