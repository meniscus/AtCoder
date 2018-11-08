# あ
N = int(input())
read_line = input().split()
a = int(read_line[0])
b = int(read_line[1])
K = int(input())
P = [int(i) for i in input().split()]

P2 = list(set(P))
if (len(P2) != len(P)) :
	# 同じ町を通過している
	print("NO")
elif (a in P) :
	# スタート地点に戻ってきている
	print("NO")
elif (b in P) :
	print("NO")
else : 
	print("YES")
	