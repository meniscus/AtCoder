N = int(input())
p = [int(i) for i in input().split()]


c = 0
is_ok = True
for i in range(N):
    if (i+1 != p[i]) :
        c += 1
    
    if (c > 2) :
        is_ok = False
        break

if (is_ok) :
    print("YES")
else :
    print("NO")