import collections

inList = input().split(" ");
human_num = int(inList[0])
relation_num = int(inList[1])

relation_factors = []
for i in range(relation_num) :
	rel_list = input().split(" ")
	relation_factors.append(int(rel_list[0]))
	relation_factors.append(int(rel_list[1]))

max_rel_count = collections.Counter(relation_factors).most_common()[0][1]
print(max_rel_count + 1)