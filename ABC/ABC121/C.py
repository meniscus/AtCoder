N,M = [int(i) for i in input().split()]
shop_info = []
for i in range(N) :
    shop_info.append([int(i) for i in input().split()])

# 安い順に取り扱えばいいはず
shop_info.sort(key=lambda x:x[0])

cost = 0
current_kan = 0
for info in shop_info:
    price = info[0]
    stock = info[1]
    if (current_kan + stock > M) :
        # 買占めはやりすぎなケース
        want_kan = M - current_kan 
        cost += price * want_kan
        break
    else :
        # 全部
        current_kan += stock
        cost += price * stock

print(cost)