l = [int(i) for i in input().split()]
A = l[0]
B = l[1]

hako = 1
while True:
	if (hako * A >= B) :
		break;
	hako += 1

print(hako)