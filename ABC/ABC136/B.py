N = int(input())

c = 0
for i in range(1,N+1) :
    s = str(i)
    if (len(s) % 2 == 1) :
        c += 1

print(c)