import collections
S = list(input())
counter = collections.Counter(S)

is_pretty = True
for v in counter.values() :
	if v % 2 != 0 :
		is_pretty = False

if (is_pretty) :
	print("Yes")
else :
	print("No")



