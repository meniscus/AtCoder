N,M,C = [int(i) for i in input().split()]
B_list = [int(i) for i in input().split()]
ok_count = 0
for i in range(N) :
    A_list = [int(i) for i in input().split()]
    tmp_sum = 0
    for m in range(M) :
        tmp_sum += A_list[m] * B_list[m]
    
    tmp_sum += C
    if (tmp_sum > 0) :
        ok_count += 1

print(ok_count)