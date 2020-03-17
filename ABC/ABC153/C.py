N,K = map(int,input().split())
monsters = [int(i) for i in input().split()]

monsters.sort(reverse=True)
for i in range(K) :
    if (i < len(monsters)) :
        monsters[i] = 0

print(sum(monsters))