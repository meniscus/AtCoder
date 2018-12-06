A,B = [int(i) for i in input().split()]
max = -1000

n = A + B
if (max < n) :
    max = n

n = A * B
if (max < n) :
    max = n

n = A - B
if (max < n) :
    max = n

print(max)