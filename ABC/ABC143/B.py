N = int(input())
li = [int(i) for i in input().split()]

c = 0

for x in range(len(li)) :
    for y in range(x+1,len(li)) :
        c += li[x]*li[y]

print(c)