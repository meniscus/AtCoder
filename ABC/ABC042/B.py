l = [int(i) for i in input().split() ]
N = l[0]
L = l[1]

words = []
_ap = words.append
for i in range(N) :
	_ap(input())

out_str = ""
_rm = words.remove
while True :
	min_word = min(words)
	out_str += min(words)
	_rm(min_word)
	
	if (len(words) == 0) :
		break;

print(out_str)

