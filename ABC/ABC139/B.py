import math

A, B = map(int,input().split())

# c = 0
# taps = 1
# while(True) :
#     # 1犠牲にしてAを得る
#     # jack = A * (taps-1) + A
#     jack = (A-1) * (taps-1) + A
#     if (jack >= B) :
#         break
    
#     taps += 1


# print(taps)

print(math.ceil((B-A) / (A-1)) + 1)