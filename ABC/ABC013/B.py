# あ
current_number = int(input())
require_number = int(input())

push_count = abs(current_number - require_number)
if push_count > abs(10 + current_number - require_number) :
	push_count = abs(10 + current_number - require_number)
if push_count > abs(10 + require_number - current_number) :
	push_count = abs(10 + require_number - current_number)

print(push_count)
