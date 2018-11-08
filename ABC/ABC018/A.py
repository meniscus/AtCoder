# あ
a1 = int(input())
a2 = int(input())
a3 = int(input())
score_list = [a1,a2,a3]
score_list.sort()
score_list.reverse()
print(score_list.index(a1) + 1)
print(score_list.index(a2) + 1)
print(score_list.index(a3) + 1)
