N,X = [int(i) for i in input().split()]
doughnut = []
for i in range(N) :
    doughnut.append(int(input()))

created = len(doughnut)
X -= sum(doughnut)
created += int(X / min(doughnut))
print(created)
