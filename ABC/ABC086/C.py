def get_distance(from_x, from_y, to_x, to_y) :
    distance_x = abs(from_x - to_x)
    distance_y = abs(from_y - to_y)
    return distance_x + distance_y

def main() :
    N = int(input())
    action_list = []
    for i in range(N) :
        action_list.append([int(i) for i in input().split()])
    
    from_x = 0
    from_y = 0
    now_t = 0

    for action in action_list :
        t = action[0]
        to_x = action[1]
        to_y = action[2]

        d = get_distance(from_x, from_y, to_x, to_y)
        if (d > (t - now_t) or (t-now_t) % 2 != d%2) :
            print("No")
            return
        
        from_x = to_x
        from_y = to_y
        now_t = t
    
    print("Yes")
    return


main()