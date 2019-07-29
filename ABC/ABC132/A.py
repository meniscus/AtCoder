def main() :

    S = input()

    S = S.replace(S[0],"")

    if (S == "") :
        print("No")
        return 

    S = S.replace(S[0],"")
    if (S == "") :
        print("Yes")
    else :
        print("No")

main()