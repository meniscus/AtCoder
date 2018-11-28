S = input()
T = input()

is_okay = False
for i in range(len(T)) :
	if (S == T) :
		is_okay = True
		break
	
	T = T[1:] + T[0]

if (is_okay) :
	print("Yes")
else :
	print("No")

