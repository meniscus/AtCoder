import collections
# あ
square_lines = [int(i) for i in input().split()]

c = collections.Counter(square_lines)

commons = c.most_common()
if (len(commons) == 1) :
	# すべての辺が同じ
	print(c.most_common()[0][0])
else :
	print(c.most_common()[1][0])