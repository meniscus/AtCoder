N = int(input())
K = int(input())
x_list = [int(i) for i in input().split()]

distance_sum = 0
for x in x_list :
    if (abs(K - x) > x) :
        distance_sum += x*2
    else :
        distance_sum += abs(K-x)*2

print(distance_sum)