import collections
N,K = [int(i) for i in input().split() ]
balls = [int(i) for i in input().split() ]

c = collections.Counter(balls)
common = c.most_common()
changed = 0

while len(common) > K :
	changed += common[-1][1]
	del common[-1]

print(changed)