N,X = [int(i) for i in input().split()]
L = [int(i) for i in input().split()]

c = 1
before_x = 0
for i in range(N) :
    if (before_x + L[i] <= X) :
        c += 1
        before_x += L[i]
    else :
        break

print(c)