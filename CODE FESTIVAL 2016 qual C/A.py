s = input()

c = s.find("C")
f = s.rfind("F")

if (c == -1 or f == -1 or f < c) :
    print("No")
else :
    print("Yes")