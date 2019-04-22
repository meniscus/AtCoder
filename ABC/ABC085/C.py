N,Y = [int(i) for i in input().split()]

# x+y+z = N
# 10000x + 5000y + 1000z = Y
# これを変形して
# 9000x + 4000y = Y - 1000Nが成り立つような
# 整数x,yの組を調べればO(N)な気がする

# y = (-9000x + Y - 1000N) / 4000

is_found = False
for x in range(0,N+1) :
    y = (-9000*x + Y - 1000* N) / 4000
    # print("x : " + str(x) + " y : " + str(y))
    if (y >= 0 and x + y <= N and float.is_integer(y)) :
        is_found = True
        print(x,int(y),int(N-x-y))
        break

if (not is_found) :
    print("-1 -1 -1")
