import collections as cl

N = int(input())
a = []
for i in range(N) :
    a.append(int(input()))
a_bk = a[:]

a.sort()

mapper = {}
key = 0
prev = -1
for a_ in a :
    if (prev == a_) :
        continue
    mapper[a_] = key
    prev = a_
    key += 1

for a_ in a_bk :
    print(mapper[a_])