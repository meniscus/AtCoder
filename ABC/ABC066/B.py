def is_even_str(s) :
    s1 = s[0:int(len(s)/2)]
    s2 = s[int(len(s)/2):]
    return (s1 == s2) 


S = input()
while len(S) > 0 :
    S =S[:-2]
    if (is_even_str(S)) :
        print(len(S))
        break
