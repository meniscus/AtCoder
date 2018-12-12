O = input()
E = input()

s = ""
for i in range(len(O)) :
    s += O[i]
    if (len(E) > i) :
        s += E[i]

print(s)