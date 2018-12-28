def main() :
    N = int(input())
    NG1 = int(input())
    NG2 = int(input())
    NG3 = int(input())
    NG = [NG1,NG2,NG3]

    if (N in NG) :
        print("NO")
        return
    

    count = 0
    while True :
        if (N == 0) :
            break

        if (N-3 not in NG and N >= 3) :
            N -= 3
            count += 1
            continue
        
        if (N-2 not in NG and N >= 2) :
            N -= 2
            count += 1
            continue
        
        if (N-1 not in NG and N >= 1) :
            N -= 1
            count += 1
            continue
        
        print("NO")
        return

    if (count <= 100) :
        print("YES")
    else :
        print("NO")


main()