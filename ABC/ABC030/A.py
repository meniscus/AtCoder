read_line = [int(i) for i in input().split()]

takahashi_rate = read_line[1] / read_line[0]
aoki_rate = read_line[3] / read_line[2]

if (takahashi_rate > aoki_rate ) :
	print("TAKAHASHI")
elif (takahashi_rate < aoki_rate) :
	print("AOKI")
else :
	print("DRAW")