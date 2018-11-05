def getProbability(tasks) :
	return 1 / tasks


tasks = int(input())
probability = getProbability(tasks)

sum = 0
for i in range(tasks+1) :
	sum += int(i * 10000)

pay = int(sum * probability)
print(pay)