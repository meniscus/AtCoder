N = int(input())
li = []
cities = []
for i in range(N) :
    inp = input().split()
    l = [inp[0], int(inp[1]), int(i+1)]
    li.append(l)
    if (l[0] not in cities) :
        cities.append(l[0])

li.sort(key=lambda x : x[0])
cities.sort()

ans = []
for c in cities :
    # hoge = list(filter(lambda x : x[0] == c, li)).sort(key=lambda x : x[1], reverse=True)
    ans += sorted(list(filter(lambda x : x[0] == c, li)),key=lambda x: x[1], reverse=True)
    # ans.extend()

for a in ans :
    print(a[2])

