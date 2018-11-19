def append_character(c,arr) :
	new_arr = []
	for s in arr :
		new_arr.append(s+c)
	
	return new_arr


N = int(input())

arr_by_step = ['a','b','c']
tmp_arr = []

for i in range(N-1) :
	tmp_arr.extend(append_character('a', list(arr_by_step)))
	tmp_arr.extend(append_character('b', list(arr_by_step)))
	tmp_arr.extend(append_character('c', list(arr_by_step)))
	
	arr_by_step = tmp_arr[:]

filtered = list(filter(lambda x:len(x) == N, arr_by_step))
filtered.sort()
for s in filtered :
	print(s)