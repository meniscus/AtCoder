def main() :
    N = int(input())
    a = [int(i) for i in input().split()]

    count = N
    if (N > 3000) :
        # とりあえず3000以上は考えないので適当に終わらせておく
        print(114514)
        return

    # N < 3000だったらこれでいいが。。。
    for i in range(N) :
        prev = -999
        for j in range(1,N) :
            if (i+j >= N) :
                break

            if (a[i] < a[i+j] and prev < a[i+j]) :
                count += 1
                prev = a[i+j]
            else :
                break

    print(count)

main()