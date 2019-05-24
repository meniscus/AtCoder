import math

S = input()
T = int(input())

x = S.count("R")
x -= S.count("L")
y = S.count("U")
y -= S.count("D")
pending_count = S.count("?")

distance = abs(x) + abs(y)
if (T == 1) :
    # 離れればいいだけなので純粋に足す
    print(distance + pending_count)
else :
    if (distance >= pending_count) :
        print(distance - pending_count)
    else :
        # 原点に戻ってきて、偶数回移動可能なら原点に戻れるはず
        a = distance - pending_count
        print(a%2)
