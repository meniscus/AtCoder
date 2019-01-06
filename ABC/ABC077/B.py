import math

def main() :
	N = int(input())
	for i in range(N,0,-1) :
		a = math.sqrt(i)
		if (a.is_integer()) :
			print(i)
			return

main()