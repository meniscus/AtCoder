N = int(input())
B_list = [int(i) for i in input().split()]
A_list = [10000000] * N

for i in range(len(B_list)) :
    B = B_list[i]
    if (min(B,A_list[i]) == B) :
        A_list[i] = B
    
    A_list[i+1] = B

# print(A_list)
print(sum(A_list))
