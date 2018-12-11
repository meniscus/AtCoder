N = int(input())

point = 999999999
for width in range(1,1001) :
    height = int(N / width)
    rest = N % width
    tmp_p = abs(width - height) + rest
    if (point > tmp_p) :
        point = tmp_p

print(point)