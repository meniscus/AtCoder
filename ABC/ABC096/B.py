li = [int(i) for i in input().split()]
K = int(input())

max_v = max(li)
max_i = li.index(max_v)
for i in range(K) :
    max_v *= 2

li[max_i] = max_v
print(sum(li))