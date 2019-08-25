A,B,C = [int(i) for i in input().split()]

remain = A - B

remain_2 = C - remain

if (remain_2 < 0) :
    print(0)
else :
    print(remain_2)