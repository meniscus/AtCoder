K,T = [int(i) for i in input().split()]
li = [int(i) for i in input().split()]

max_cake = max(li)
without_cake = sum(li) - max_cake

if (max_cake - without_cake - 1 < 0) :
    print(0)
else :
    print(max_cake - without_cake - 1)