def main() :
	N = int(input())
	
	while N > 0 :
		if (N % 7 == 0 or N % 4 == 0) :
			return "Yes"
		N = N-7

	return "No"

print(main())