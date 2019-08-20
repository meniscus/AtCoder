N  = int(input())
A_list = []
primary_max = 0
secondary_max = 0

for i in range(N) :
    n = int(input())
    if (primary_max <= n) :
        if (primary_max == secondary_max) :
            primary_max = n
        else :
            secondary_max = primary_max
            primary_max = n
    elif (secondary_max < n and n < primary_max) :
        secondary_max = n

    A_list.append(n)

for a in A_list :
    if (a == primary_max) :
        print(secondary_max)
    else :
        print(primary_max)

