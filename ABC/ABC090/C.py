def main() :
    N,M = [int(i) for i in input().split()]

    if (N > 2) :
        rows = N-2
    elif (N == 1) :
        rows = 1
    else :
        print("0")
        return
    
    if (M > 2) :
        cols = M-2
    elif (M == 1):
        cols = 1
    else :
        print("0")
        return

    print(rows * cols)

main()