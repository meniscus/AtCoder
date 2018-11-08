# あ
N = list(input())

out_str = ""
for i in range(len(N)) :
	if (N[i] == "1") :
		out_str += "9"
	else :
		out_str += "1"

print(out_str)