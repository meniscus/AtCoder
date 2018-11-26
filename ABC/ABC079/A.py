N_str = input()
N1 = N_str[0:3]
N2 = N_str[1:4]
if (len(set(list(N1))) == 1 or len(set(list(N2))) == 1) :
	print("Yes")
else :
	print("No")
