A,K = [int(i) for i in input().split()]



money = A
days = 1
if (K == 0) :
    print(2000000000000 - A)
else :
    while (True) :
        money += 1 + K * money
        if (money >= 2000000000000) :
            print(days)
            break
        days += 1