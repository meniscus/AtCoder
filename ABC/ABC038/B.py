d1 = [int(i) for i in input().split()]
d2 = [int(i) for i in input().split()]

if (d1[0] == d2[0] or d1[0] == d2[1] or d1[1] == d2[0] or d1[1] == d2[1]) :
	print("YES")
else :
	print("NO")