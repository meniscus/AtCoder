def add_alpha(char, add) :
    code = ord(char) + add
    if (code >= 91) :
        code -= 26
    return chr(code)


def main() :
    N = int(input())
    S = input()

    out = ""
    for s in S:
        out += add_alpha(s,N)

    print(out)

main()