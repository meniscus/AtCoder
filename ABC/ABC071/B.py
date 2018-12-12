S = input()
msg = "None"
for i in range(26) :
    c = chr(ord("a")+i)
    if(S.find(c) == -1) :
        msg = c
        break

print(msg)