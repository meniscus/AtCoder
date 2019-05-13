N,M,A,B = [int(i) for i in input().split()]

for day in range(M) :
    if (N <= A) :
        N += B

    N -= int(input())
    if (N < 0) :
        print(day+1)
        exit()
    
print("complete")