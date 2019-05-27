N = int(input())
V_list = [int(i) for i in input().split()]
C_list = [int(i) for i in input().split()]

max_point = 0
for i in range(N) :
    p = V_list[i] - C_list[i]
    if (p > 0) :
        max_point += p

print(max_point)