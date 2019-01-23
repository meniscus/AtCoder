def f(n) :
    if (n % 2 == 0) :
        return n // 2
    else :
        return 3 * n + 1

def main() :
    # 10^6なので愚直でいいはず。
    s = int(input())
    li = [s]
    loop_count = 1
    while(True) :
        loop_count += 1
        n = f(s)
        if (li.count(n) > 0) :
            print(loop_count)
            return
        else :
            li.append(n)
            s = n

    

main()