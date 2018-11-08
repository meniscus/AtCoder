# あ
in_str_list = list(input())

out_str = ""
tmp_str = in_str_list[0]
tmp_count = 0
for i in range(len(in_str_list)) :
	if (tmp_str != in_str_list[i]) :
		out_str += tmp_str
		out_str += str(tmp_count)
		tmp_str = in_str_list[i]
		tmp_count = 0
	
	tmp_count += 1

out_str += tmp_str
out_str += str(tmp_count)
tmp_str = in_str_list[i]
tmp_count = 0

print(out_str)
		