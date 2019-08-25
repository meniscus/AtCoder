def main () :

    M,D = map(int,input().split())

    if (D <= 10) :
        print("0")
        return
    
    count = 0
    for m in range(1,M+1) :
        for d in range(11, D+1) :
            str_d = str(d)
            d1 = int(str_d[0])
            d10 = int(str_d[1])

            if (d1 < 2 or d10 < 2) :
                continue

            if (m == d1 * d10) :
                count += 1
    
    print(count)






main()

