cats,animals,expect_cats = [int(i) for i in input().split()]

if (cats > expect_cats) :
	print("NO")
elif (cats+animals < expect_cats) :
	print("NO")
else :
	print("YES")