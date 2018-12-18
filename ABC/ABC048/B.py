a,b,x = [int(i) for i in input().split()]

res = int(b//x) - int((a-1)//x)
print(res)