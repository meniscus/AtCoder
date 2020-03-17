import collections as cl

N = int(input())
A_li = [int(i) for i in input().split()]
mc = cl.Counter(A_li).most_common()
if (mc[0][1] == 1) :
    print("YES")
else :
    print("NO")