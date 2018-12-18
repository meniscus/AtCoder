N,A,B = [int(i) for i in input().split()]
all_sum = 0
for i in range(1,N+1) :
    degit_sum = sum([int(i) for i in list(str(i))])
    if (A <= degit_sum and degit_sum <= B ) :
        all_sum += i

print(all_sum)