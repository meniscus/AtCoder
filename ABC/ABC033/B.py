N= int(input())
cities = []
sum = 0
for i in range(N) :
	read_line = input().split()
	sum += int(read_line[1])
	cities.append([read_line[0], int(read_line[1])])

metro = "atcoder"
for i in range(N) :
	if cities[i][1] * 2 > sum :
		metro = cities[i][0]
		break

print(metro)