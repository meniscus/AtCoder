# あ
baggages = int(input())

carry_count = int(baggages / 2)
if (baggages % 2 == 1) :
	carry_count += 1

print(carry_count)
