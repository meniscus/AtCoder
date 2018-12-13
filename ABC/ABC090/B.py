A,B = [int(i) for i in input().split()]
count = 0
for i in range(A,B+1) :
    s = str(i)

    is_ok = True
    # lenが奇数でもいいはず。真ん中は関係ないので
    for n in range(len(s) // 2) :
        if (s[n] != s[-n-1]) :
            is_ok = False
            break
    if (is_ok):
        count += 1

print(count)