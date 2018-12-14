import collections as cl
N = int(input())
a_li = [int(i) for i in input().split()]
a_li2 = [i-1 for i in a_li]
a_li3 = [i+1 for i in a_li]
a_li.extend(a_li2)
a_li.extend(a_li3)
c = cl.Counter(a_li)
print(c.most_common()[0][1])

# keys = list(c.keys())
# max_sum = 0
# if (len(c) == 1) :
#     # 1種類しかない
#     print(len(a_li))
# elif (len(c) == 2) :
#     # 2種類ある
#     if (abs(int(keys[0]) - int(keys[1])) <= 2 ) :
#         # 差が2以下なら全部同じ値にできる
#         print(len(a_li))
#     else :
#         # 差が2より大きいなら多いほうの個数が最大
#         if (int(c[keys[0]]) > int(c[keys[1]])) :
#             print(c[keys[0]])
#         else :
#             print(c[keys[1]])
# else :
#     # この思想はNG。keys[k]からkeys[k+2]の差が2以下じゃないと成り立たない。
#     for k in range(len(c) -2 ) :
#         sum_v = c[keys[k]] + c[keys[k+1]] + c[keys[k+2]]
#         if (max_sum < sum_v) :
#             max_sum = sum_v
    
#     print(max_sum)



