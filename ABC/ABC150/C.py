import itertools as it

N = int(input())
P = [int(i) for i in input().split()]
Q = [int(i) for i in input().split()]
a = -1
b = -1

li = list(it.permutations(P,N))
li.sort()
for n in range(len(li)) :
    l = li[n]
    # print(l)
    is_P = True
    is_Q = True
    for i in range(N) :
        if (P[i] != l[i]) :
            is_P = False
        if (Q[i] != l[i]) :
            is_Q = False
        if (not(is_P) and not(is_Q)) :
            break
    if (is_P) :
        a = n+1
    if (is_Q) :
        b = n+1

# print(a,b)
print(abs(a-b))

