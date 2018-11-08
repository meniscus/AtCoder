def is_war_by_list(x_list, y_list) :
	max_x = max(x_list)
	min_y = min(y_list)
	
	if (max_x < min_y) :
		return False
	else :
		return True

def is_war_by_number(x,y,z) :
	if (x < z and z <= y) :
		return False
	else :
		return True
	

# あ
read_line = [int(i) for i in input().split()]
N = read_line[0]
M = read_line[1]
X = read_line[2]
Y = read_line[3]

x_list = [int(i) for i in input().split()]
y_list = [int(i) for i in input().split()]

if (is_war_by_list(x_list,y_list) or is_war_by_number(X,Y, min(y_list))) :
	print("War")
else :
	print("No War")