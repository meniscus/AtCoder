N = int(input())
v_list = list(map(int,input().split()))

# 合成すると総価値が下がるので、価値の低いものから使っていくとダメージが少ないはず。。。
# N<50なので愚直にやっていいはず
v_list.sort()

s = v_list.pop(0)

for v in v_list :
    s = (s + v) / 2.0

print(s)