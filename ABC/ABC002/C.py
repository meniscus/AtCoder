inList = input().split(" ");
p1_x = 0
p1_y = 0
p2_x = int(inList[2]) - int(inList[0])
p2_y = int(inList[3]) - int(inList[1])
p3_x = int(inList[4]) - int(inList[0])
p3_y = int(inList[5]) - int(inList[1])

area = abs((p2_x * p3_y - p2_y * p3_x) / 2)

print(area)