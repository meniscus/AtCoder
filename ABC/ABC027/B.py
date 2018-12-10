# あ
def main() :
	N = int(input())
	population = [int(i) for i in input().split()]

	if (sum(population) % N != 0) :
		print("-1")
		return

	population_per_island = int(sum(population) / N)

	depend_bridge = 0
	for i in range(1,len(population)) :
		if (sum(population[:i]) != population_per_island * len(population[:i]) ) :
			depend_bridge += 1
		
	print(depend_bridge)

main()