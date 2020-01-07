A,B,K = map(int,input().split())

# for i in range(K) :
#     if (A >= 1) :
#         A -= 1
#     elif (B >= 1) :
#         B -= 1

# print(A,B)

if (A <= K) :
    K -= A
    A = 0
else :
    A -= K
    K = 0

if (B <= K) :
    K -= B
    B = 0
else :
    B -= K
    K = 0

print(A,B)