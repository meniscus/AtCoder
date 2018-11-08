# s = [*input()]
s = list(input())
count = int(input())

reverse_def = []
for i in range(count) :
	reverse_def.append(input().split())

for item in reverse_def :
	from_index = int(item[0]) - 1
	to_index = int(item[1])
	s[from_index:to_index] = s[from_index:to_index][::-1]

print(''.join(s))
