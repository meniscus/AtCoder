L,R = [int(i) for i in input().split()]

length = min(2019,R-L)
# 右端値はL+2019か、R-Lでよい
R = L + length

ans = 9999999999999999
for i in range(L,R+1) :
    for j in range(i+1,R+1) :
        v = (i * j) % 2019
        if (v < ans) :
            ans = v

print(ans)