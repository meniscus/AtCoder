a,b = [i for i in input().split()]
is_honest = True
if (a == 'H') :
	is_honest = True
else :
	is_honest = False

if (b == 'H' and is_honest) :
	print("H")
elif (b == 'H' and not is_honest) :
	print("D")
elif (b == 'D' and is_honest) :
	print("D")
else :
	print("H")