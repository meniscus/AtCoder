N,L = map(int,input().split())

taste_all = ((L+1-1) + (L+N-1)) * N // 2

diff = 99999999
ans_taste = 0
ans_i = 9999
for i in range(1,N+1) :
    taste = taste_all - (L+i-1)
    d = abs(taste_all - taste)
    if (d < diff ) :
        diff = d
        ans_taste = taste
        ans_i = i

print(ans_taste)
