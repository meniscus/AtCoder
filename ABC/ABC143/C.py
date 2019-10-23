N = int(input())
S = input()

prev = S[0]
c = 1
for s in S :
    if (prev != s) :
        prev = s
        c += 1

print(c)
    