N = int(input())
sum = 0
for i in range(N) :
    seats = [int(i) for i in input().split()]
    sum += seats[-1] - seats[0] + 1

print(sum)