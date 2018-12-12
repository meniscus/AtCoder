import collections

N,M = [int(i) for i in input().split()]
node = []
for ii in range(M) :
    node.extend([int(i) for i in input().split()])

c = collections.Counter(node)
for i in range(1,N+1) :
    print(c[i])