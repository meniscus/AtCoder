n = int(input())
p = [int(i) for i in input().split()]

count = 0
for i in range(n-2) :
    l = p[i:i+3]
    if (min(l) != l[1] and max(l) != l[1]) :
        count += 1

print(count)