def main() :
    N = int(input())
    H_list = [int(i) for i in input().split()]    

    max_step = 0
    current_step = 0

    prev_H = H_list[0]
    for i in range(1,N) :
        H = H_list[i]
        # print(prev_H,H)
        if (prev_H  >= H) :
            # print(True)
            current_step += 1
        else :
            if (max_step <= current_step) :
                max_step = current_step

            current_step = 0
        prev_H = H
        # print(H,current_step,max_step)

    if (max_step <= current_step) :
        max_step = current_step
    
    print(max_step)





main()


def gomi() :
    N = int(input())
    H_list = [int(i) for i in input().split()]

    # 単調減少区間の最大長を求めればよい -> どうやって？
    # 愚直に書いたら間に合わないはず
    max_downs = 0
    current_downs = 0
    prev_H = 999999999999999 
    for H in H_list :
        if (prev_H >= H ) :
            current_downs += 1
            prev_H = H
        else :
            if (current_downs > max_downs ) :
                max_downs = current_downs

            current_downs = 0
            prev_H = 999999999999999
        
        print(current_downs, max_downs)

    if (current_downs > max_downs ) :
        max_downs = current_downs

    # 着地を1で数えちゃったので引く
    print(max_downs-1)
