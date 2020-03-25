N = int(input())
P_list = [int(i) for i in input().split()]

# cnt = 1 # 1件目は必ず合致するので

# for i in range(1,len(P_list)) :
#     pi = P_list[i]
#     is_match = True
#     for j in range(i) : # Pi==Pjは必ず正なのでジャッジ不要
#         pj = P_list[j]
#         if (pi > pj) :
#             is_match = False
#             break
    
#     if (is_match) :
#         cnt += 1

cnt = 1 # 1件目は必ず合致するので
min_map = [P_list[0]]
min_value = P_list[0]
for i in range(1,len(P_list)) :
    min_value = min(min_value,P_list[i])
    min_map.append(min_value)

# print(min_map)
for i in range(1,len(P_list)) :
    if (min_map[i] >= P_list[i]) :
        cnt += 1



print(cnt)