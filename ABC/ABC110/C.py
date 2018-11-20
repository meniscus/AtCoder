S = input()
T = input()

out_str = "Yes"

indexes_s_all = []
indexes_t_all = []
for i in range(26) :
	c = chr(ord('a') + i)
	indexes_s = [n for n, x in enumerate(list(S)) if x == c]
	indexes_t = [n for n, x in enumerate(list(T)) if x == c]
	indexes_s_all.append(indexes_s)
	indexes_t_all.append(indexes_t)

indexes_s_all.sort()
indexes_t_all.sort()
if (indexes_s_all == indexes_t_all) :
	print("Yes")
else :
	print("No")