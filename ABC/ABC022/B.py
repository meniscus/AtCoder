import math
# あ
flower_count = int(input())
flower_list = []
for i in range(flower_count) :
	flower_list.append(int(input()))

li = list(set(flower_list))


print(len(flower_list) - len(li))