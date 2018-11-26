def main() :
	S = input()
	if (S[0] != "A") :
		print("WA")
		return
	
	if (list(S).count("A") != 1) :
		print("WA")
		return
	
	S2 = list(S[2:-1])
	if (S2.count("C") != 1) :
		print("WA")
		return
	
	for s in list(S) :
		if (s == "A" or s == "C") :
			continue
		
		if (s.isupper()) :
			print("WA")
			return
	
	print("AC")


main()