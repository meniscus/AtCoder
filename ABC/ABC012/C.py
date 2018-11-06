# あ

required = 2025
wrong_answer = int(input())
diff = required - wrong_answer

li = []
for i in range(1,10) :
	for j in range(1,10) :
		if i * j == diff :
			li.append(str(i) + " x " + str(j))
			li.append(str(j) + " x " + str(i))

li = list(set(li))
li.sort()

for s in li :
	print(s)