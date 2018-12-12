W,a,b = [int(i) for i in input().split()]

if (a+W <= b) :
    print(b-(a+W))
elif (a <= b and b <= a+W) :
    print(0)
else :
    print(a-(b+W))