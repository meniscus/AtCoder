A,B = [int(i) for i in input().split()]

n = (A + B) / 2

if (float.is_integer(n)) :
    print(int(n))
else :
    print("IMPOSSIBLE")