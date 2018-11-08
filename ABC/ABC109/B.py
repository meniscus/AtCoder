N = int(input())
words = []
for i in range(N) :
	words.append(input())

first_word = words[0][0]
last_word = ""
is_okay = True

tmp_words = list(set(words))
if (len(tmp_words) != len(words)) :
	is_okay = False

for s in words :
	if (first_word != s[0]) :
		is_okay = False
		break
	
	first_word = s[-1]


if(is_okay) :
	print("Yes")
else :
	print("No")