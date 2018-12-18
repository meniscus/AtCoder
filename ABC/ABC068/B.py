import math
N = int(input())

# 実際Nもいらない
for i in range(N) :
    if (N == 1) :
        # この実装が汚い。。。
        print(1)
        break

    if (N < math.pow(2,i)) :
        print(int(math.pow(2,i-1)))
        break
