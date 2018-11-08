# あ
numbers = [int(i) for i in input().split()]

A = numbers[0]
B = numbers[1]

if (A % 2 == 1 and B % 2 == 1) :
	print("Yes")
else :
	print("No")