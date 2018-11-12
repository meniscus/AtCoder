import math
# 
N = int(input())
radius_list = []
for i in range(N,0,-1) :
	radius_list.append(int(input()))

radius_list.sort(reverse=True)
sqrt_area = 0
for i in range(len(radius_list)) :
	sqrt_area += math.pow(-1, i) * math.pow(radius_list[i], 2)

print(sqrt_area * math.pi)
