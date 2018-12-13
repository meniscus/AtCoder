s = list(input())
t = list(input())

s2 = ''.join(sorted(s))
t2 = ''.join(sorted(t,reverse=True))
if (s2 < t2) :
    print("Yes")
else :
    print("No")
