def main() :

    N,T,E = [int(i) for i in input().split()]
    clocks = [int(i) for i in input().split()]

    for i in range(N) :
        base_clock = clocks[i]
        clock = clocks[i]

        while (clock <= T + E) :
            if (T-E <= clock and clock <= T+E) :
                print(i+1)
                return

            clock += base_clock

    print(-1)

main()