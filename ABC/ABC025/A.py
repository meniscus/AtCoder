# あ
chars = list(input())
index = int(input()) - 1
fav_list = []

for c in chars :
	for c2 in chars :
		fav_list.append(c+ c2)


print(fav_list[index])