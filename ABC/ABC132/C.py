N = int(input())
d = [int(i) for i in input().split()]

d.sort()

half_len = len(d)//2
l = d[half_len-1]
r = d[half_len]

if (r-l > 0) :
    print(r-l)
else :
    print(0)