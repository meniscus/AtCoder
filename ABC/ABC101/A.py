S = input()

t = 0
for s in list(S) :
	if (s == "+") :
		t += 1
	else :
		t -= 1

print(t)