N,K = map(int,input().split())
A_list = [int(i) for i in input().split()]

# 自分自身の中で、転倒するような数 * N-1
# 最後の繰り返しは、転倒しないので別途計算
## これじゃダメで、転倒数はどんどん減少していくはず。

# 順序が関係するのは最初のブロックだけ
# あとは、繰り返しになる(繰り返し数が減っていく)

# まず、順序を含めた合算個数を調べる
count_with_seq = 0
deal = 0
for i in range(N) :
    ai = A_list[i]
    for k in range(i+1,N) :
        deal += 1
        ak = A_list[k]
        if (ai > ak) :
            # print(ai,ak)
            count_with_seq += 1

count_without_seq = 0
for ai in A_list :
    for ak in A_list :
        if (ai > ak) :
            count_without_seq += 1

# print(count_with_seq,count_without_seq)

# これらの塊の繰り返し数は、
# 初項：N回
# 初項以降 : sum(k) (1<=K<=n-1) 

total_count = count_with_seq * K
# print(total_count)
rep = (1 + (K-1)) * (K-1) // 2
total_count += count_without_seq * rep
# print(rep)
print(total_count % 1000000007)