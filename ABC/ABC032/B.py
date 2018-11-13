s = input()
pass_len = int(input())
pass_list = []
for i in range(len(s) - pass_len + 1) :
	pass_list.append(s[i:pass_len+i])

pass_list = list(set(pass_list))
print(len(pass_list))