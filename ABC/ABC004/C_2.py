card_list = ['1','2','3','4','5','6']
request_actions = int(input())

request_actions_mod_30 = request_actions % 30

for i in range(request_actions_mod_30) :
	from_index = int(i % 5)
	to_index = int(i % 5) + 1
	card_list[from_index],card_list[to_index] = card_list[to_index],card_list[from_index]

out_str = ""
for i in range(len(card_list)) :
	out_str = out_str + card_list[i]

print(out_str)