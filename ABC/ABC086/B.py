import math
a,b = input().split()
n = int(a + b)

if (math.sqrt(n).is_integer()) :
    print("Yes")
else :
    print("No")