r,D,x2000 = [int(i) for i in input().split()]

x = x2000
for i in range(1,11) :
    x = (r * x - D)
    print(x)

