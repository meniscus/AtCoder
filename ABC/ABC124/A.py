A,B = [int(i) for i in input().split()]

deal_count = 2
get_coin = 0

for i in range(deal_count) :
    if (A == max([A,B])) :
        get_coin += A
        A -= 1
    else :
        get_coin += B
        B -= 1

print(get_coin)