import collections

# あ
vote_count = int(input())

vote_detail = []
for i in range(vote_count) :
	vote_detail.append(input())

c = collections.Counter(vote_detail)

print(c.most_common()[0][0])
