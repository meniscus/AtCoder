N,K = [int(i) for i in input().split()]
S = input()

out_str = ""
for i in range(N) :
    if (i == K-1) :
        out_str += S[i].lower()
    else :
        out_str += S[i]

print(out_str)