# あ
read_line = input().split()

a = int(read_line[0])
b = int(read_line[1])
c = int(read_line[2])

canSum = False
canSub = False

if (a + b == c) :
	canSum = True

if (a - b == c) :
	canSub = True

if (canSum and canSub) :
	print("?")
elif (canSum and not canSub) :
	print("+")
elif (not canSum and canSub) :
	print("-")
else :
	print("!")