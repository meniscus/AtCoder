import math

X = int(input())
max_exp = 0

for b in range(1,50) :
    for p in range(2,10) :
        exp = int(math.pow(b,p))
        if (exp > X) :
            continue
        if (max_exp < exp)  :
            max_exp = exp

print(max_exp)