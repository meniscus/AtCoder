l = [int(i) for i in input().split()]
legs = l[1]
humans = l[0]
bba = 0

if (legs % 2 == 1 ) :
	bba = 1
	legs -= 3
	humans -= 1

# 2 * n + 4 * (humans -n) = legs
adults = int((4 * humans - legs) / 2)
if adults >= 0 and humans-adults >= 0 :
	out_str = str(int(adults)) + " " + str(bba) + " " + str(humans-adults)
	print(out_str)
else :
	print("-1 -1 -1")