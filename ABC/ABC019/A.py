# あ
age_list = [int(s) for s in input().split()]
age_list.remove(max(age_list))
age_list.remove(min(age_list))
print(age_list[0])