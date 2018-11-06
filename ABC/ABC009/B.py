
# あ
dish_count = int(input())

price_list = []
for i in range(dish_count) :
	price_list.append(int(input()))

price_list.sort()

price = price_list[-1]
for current_price in price_list[::-1] :
	if (current_price != price) :
		price = current_price
		break

print(price)
