def main() :
    hit_list = [int(i) for i in input().split()]
    bonus_num = int(input())
    takahashi_list = [int(i) for i in input().split()]

    matched_list = list(set(hit_list) & set(takahashi_list))
    match_count = len(matched_list)
    if (match_count == 6) :
        print(1)
    elif (match_count == 5 and bonus_num in takahashi_list) :
        print(2)
    elif (match_count == 5 and bonus_num not in takahashi_list) :
        print(3)
    elif (match_count == 4) :
        print(4)
    elif (match_count == 3) :
        print(5)
    else :
        print(0)


main()