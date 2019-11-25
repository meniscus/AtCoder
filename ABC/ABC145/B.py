def main() :
    N = int(input())
    S = input()

    if (N % 2 == 1) :
        print("No")
        return

    n = N // 2
    s = S[0:n]
    if (s+s == S) :
        print("Yes")
    else :
        print("No")

main()