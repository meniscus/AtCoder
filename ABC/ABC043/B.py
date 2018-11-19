s = input()

out_str = ""
for i in range(len(s)) :
	if (s[i] == "B") :
		if (len(out_str) != 0) :
			out_str = out_str[:-1]
		continue
	
	out_str += s[i]

print(out_str)