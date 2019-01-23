import collections as cl

N = int(input())
sticks = [int(i) for i in input().split()]

sticks.sort(reverse=True)

w = 0
h = 0

for k,v in sorted(cl.Counter(sticks).items(), key=lambda x: x[0], reverse=True):
    if (v < 2) :
        continue
    
    if (v >= 4) :
        # 4本以上あれば正方形が作れる
        if (w == 0) :
            w = k
            h = k
        else :
            h = k
        break
    
    if (v >= 2) :
        if (w == 0) :
            w = k
        else :
            h = k
            break


print(w*h)