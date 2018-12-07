import math
D,N = [int(i) for i in input().split()]
if (N != 100) :
    print(int(math.pow(100,D) * N))
else :
    # N = 100のときは割り切れてしまう(Dの条件に反してしまう)ので+1したものをかける
    print(int(math.pow(100,D) * 101))