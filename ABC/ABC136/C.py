def main() :

    N = int(input())
    H_list = [int(i) for i in input().split()]

    # ひっくり返して、単調増加だったらNGと考える
    H_list.reverse()
    c = 0
    for i in range(len(H_list)-1) :
        d = H_list[i+1] - H_list[i]
        if (d >= 2) :
            # 増分2以上はどうしようもない
            print("No")
            return

        if (d == 1) :
            # 増分1なら削ればいい
            c += 1
            H_list[i+1] = H_list[i+1] - 1
    
    print("Yes")

main()