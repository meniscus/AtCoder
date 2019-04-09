N,Q = [int(i) for i in input().split()]
S = input()
q_list = []
for i in range(Q) :
    q_list.append([int(i) for i in input().split()])


## No.5
# n番目までに何回ACって出るか調べたらO(N)で済むのでは？
c = 0
ac_list = []
for i in range(len(S)) :
    # Cの位置を基準にする
    if (S[i] == "C" and i > 0 and S[i-1] == "A") :
        c += 1
        ac_list.append(c)
    else :
        ac_list.append(c)

for item in q_list :
    # XXXXA | C だったケースは除外するので、右端は-1する
    ac_count = ac_list[item[1]-1] - ac_list[item[0]-1]
    print(ac_count)



## No.4
# a_indexes = []
# # 下処理として、Aの場所だけ覚えておく
# for i in range(len(S)) :
#     if (S[i] == "A") :
#         a_indexes.append(i)

# # 幅に応じて、Aの次がCかどうかを判定する
# for item in q_list :
#     from_index = item[0]
#     to_index = item[1]
#     # 次の文字がCであることを調べるので、toは1文字手前にする
#     target_indexes = [i for i in a_indexes if i >= from_index-1 and i < to_index-1]
#     ac_count = 0
#     for index in target_indexes :
#         if (S[index+1] == "C") :
#             ac_count += 1
    
#     print(ac_count)


## No.1  もちろんTLE。。。
# for item in q_list :
#     from_index = item[0]
#     to_index = item[1]
#     search_str = S[from_index-1:to_index]
#     find_index = 0
#     ac_count = 0
#     while(find_index != -1) :
#         find_index = search_str.find("AC",find_index)
#         if (find_index != -1) :
#             ac_count += 1
#             find_index += 1
#     print(ac_count)

## No.2,3
# for item in q_list :
#     from_index = item[0]
#     to_index = item[1]
#     search_str = S[from_index-1:to_index]
    # print(search_str.replace("AC","X").count("X"))
    # print(search_str.count("AC"))
        
