import collections as cl

A,B,C,D = [int(i) for i in input().split()]
arr = [0]*100

for i in range(A,B) :
    arr[i] += 1

for i in range(C,D) :
    arr[i] += 1

c = cl.Counter(arr)
print(c[2])
