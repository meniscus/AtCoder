def main() :
    N,D = [int(i) for i in input().split()]

    # if (N <= 2*D+1) :
    #     print(1)

    # for i in range(N) :
    #     n = (1 + 2*D) * i
    #     if(N <= n) :
    #         print(i)
    #     break

    for i in range(N+1) :
        n = (1 + 2*D) * i
        if(N <= n) :
            print(i)
            break


main()