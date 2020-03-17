import math

def get_count(H, count) :

    if (H == 1) :
        return 1


    return 2 * get_count(H // 2, count) + 1

def main() :
    H = int(input())
    c = get_count(H,0)
    print(c)

main()