N = int(input())
dama = 0.0
for i in range(N):
    x,u = input().split()
    if (u == "BTC") :
        dama += float(x) * 380000.0
    else :
        dama += float(x)

print(dama)
