def main() :
    N = int(input())
    count_100 = N // 10
    remainder = N % 10
    if (remainder > 6) :
        print(int((N//10) + 1)* 100)
    else :
        print(int(N//10) * 100 + remainder * 15)
        


main()