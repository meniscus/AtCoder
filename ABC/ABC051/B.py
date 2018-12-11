K,S = [int(i) for i in input().split()]
patterns = 0

for x in range(K+1) :
    for y in range(K+1) :
        z = S - x - y
        if (0 <= z and z <= K) :
            patterns += 1

print(patterns)
