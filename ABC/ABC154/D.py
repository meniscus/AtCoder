N,K = map(int,input().split())
dice_list = [int(i) for i in input().split()]
wa_list = [0]
for dice in dice_list :
    # prob = 0
    # for i in range(dice) :
    #     prob += (i+1) * (1/(dice))
    prob = (1+dice) / 2
    wa_list.append(wa_list[-1] + prob)

max_p = -1
for i in range(N-K+1) :
    p = wa_list[i+K] - wa_list[i]
    if (max_p < p) :
        max_p = p

print(max_p)



