def main() :
    N = int(input())

    # 式変形していいかんじに下ごしらえして、
    # 2変数分のループで全探索する。O(3500^2)なら間に合うはず。

    for h in range(1,3501) :
        for n in range(1,3501) :
            if ((4*h*n - N*n - N*h) == 0) :
                continue

            omega = (N * h * n * 1.0) / ((4*h*n - N*n - N*h) * 1.0)
            if (omega.is_integer() == True and omega >= 0) :
                print(h,n,int(omega))
                return

main()