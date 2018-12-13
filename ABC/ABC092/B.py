N = int(input())
D,X = [int(i) for i in input().split()]
eaten_day = []
a_li = []
for i in range(N) :
    a_li.append(int(input()))

for i in range(N) :
    for d in range(1,D+1) :
        eat_day = (d-1) * a_li[i] + 1
        if (0 < eat_day and eat_day <= D) :
            eaten_day.append(eat_day)
print(len(eaten_day) + X)
