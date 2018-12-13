import collections as cl
N = int(input())
S = input()

max_count = -1
max_index = -1
for i in range(N) :
    c1 = cl.Counter(list(S[0:i]))
    c2 = cl.Counter(list(S[i:]))
    if (len(c1.keys() & c2.keys()) > max_count) :
        max_count = len(c1.keys() & c2.keys())
        max_index = i

print(max_count)