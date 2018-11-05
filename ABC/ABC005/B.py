takoyaki_count = int(input())

takoyaki_birth_list = []
for i in range(takoyaki_count) :
	takoyaki_birth_list.append(int(input()))

print(min(takoyaki_birth_list))