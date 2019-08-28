def checkLR(current_line, current_pos) :

    if (0 < current_pos) :
        L = current_line[current_pos-1]
        if (L == "-") :
            return "L"

    if (current_pos + 1 < len(current_line) ) :
        R = current_line[current_pos+1]
        if (R == "-") :
            return "R"
    
    return "N"
    


def main() :

    N,L = map(int,input().split())
    lines = []
    for i in range(L) :
        lines.append(input())

    atari = input()
    # print(lines)
    # print(atari)

    pos = atari.find("o")

    for i in range(L-1,-1,-1) :
        res = checkLR(lines[i], pos)
        if (res == "L") :
            pos -= 2
        elif (res == "R") :
            pos += 2

        # print(res)

    print((pos//2) + 1)

main()