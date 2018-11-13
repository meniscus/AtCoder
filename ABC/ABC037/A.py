l = [int(i) for i in input().split()]
A,B,C = l[0],l[1],l[2]

cheaper_price = 0
if (A < B) :
	cheaper_price = A
else :
	cheaper_price = B

print(int(C/cheaper_price))
