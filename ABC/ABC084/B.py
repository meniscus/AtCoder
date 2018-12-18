A,B = [int(i) for i in input().split()]
S = input()

if (S[0:A].isdecimal() and S[A] == '-' and S[A+1:].isdecimal()) :
    print("Yes")
else :
    print("No")