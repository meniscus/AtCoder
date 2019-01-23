x,a,b = [int(i) for i in input().split()]

if (abs(x - a) > abs(x - b)) :
    print("B")
else :
    print("A")