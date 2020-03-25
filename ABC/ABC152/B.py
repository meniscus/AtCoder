a,b = [int(i) for i in input().split()]
if (a > b) :
    a,b = b,a

print(str(a) * b)