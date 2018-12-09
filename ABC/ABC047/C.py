S = input()

prev_color = S[0]
count = 0
for i in range(len(S)) :
	current_color = S[i]
	if (prev_color == current_color) :
		continue
	else :
		prev_color = current_color
		count += 1

print(count)