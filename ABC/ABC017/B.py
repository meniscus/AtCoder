# あ
word = input()

is_choku = True
if len(word) == 0 :
	print("YES")
else :
	for i in range(len(word)) :
		if (word[i] in ['o', 'k', 'u']) :
			continue
		elif (len(word) > i + 1 and word[i] == 'c' and word[i+1] == 'h') :
			continue
		elif (word[i] == 'h' and word[i-1] == 'c') :
			continue
		else :
			is_choku = False
			break

if (is_choku) :
	print("YES")
else :
	print("NO")