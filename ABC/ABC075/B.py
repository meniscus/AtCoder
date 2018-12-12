def draw_map(count_map, row_index, col_index) :
	for i in range(row_index-1, row_index+2) :
		if (i < 0 or len(count_map) <= i) :
			continue
		for j in range(col_index-1, col_index+2) :
			if (j < 0 or len(count_map[0]) <= j) :
				continue
			count_map[i][j] += 1
	
	return count_map
    				
    			

H,W = [int(i) for i in input().split()]
mines = []
for i in range(H) :
	mines.append(input())

# 白地図を用意して、1ずつ足す
# 空きマスだったら数字に置き換える
count_map = [[0 for i in range(W)] for j in range(H)]
for i in range(H) :
	for j in range(W) :
		if (mines[i][j] == "#") :
			mine_map = draw_map(count_map,i,j)

for i in range(H) :
	out_line = ""
	for j in range(W) :
		if (mines[i][j] == ".") :
			out_line += str(count_map[i][j])
		else :
			out_line += "#"
	print(out_line)
    		
