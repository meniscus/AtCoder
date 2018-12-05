def main() :
	S = input()
	K = int(input())

	is_1 = True
	for i in range(K) :
		if (len(S) < i) :
			break

		# print("S[i] : " + S[i])
		if (S[i] != "1") :
			is_1 = False
			break

	if (is_1) :
		print("1")
		return

	for i in range(len(S)) :
		if (S[i] == "1") :
			continue

		print(S[i])
		break


main()
