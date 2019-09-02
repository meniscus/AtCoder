N = int(input())
A_list = [int(i) for i in input().split()]
B_list = [int(i) for i in input().split()]

killed = 0
for i in range(N) :
    brave = B_list[i]
    monster = A_list[i]
    # print(brave,monster)
    if (brave >= monster) :
        # 殺りきれる場合
        killed += monster
        brave -= monster
        monster = A_list[i+1]
        if (brave >= monster) :
            killed += monster
            brave -= monster
            monster = 0
        elif (brave < monster) :
            # 殺りきれない場合
            killed += brave
            monster -= brave # この処理はいる
        A_list[i+1] = monster
            
    elif (brave < monster) :
        # 殺りきれない場合
        killed += brave
        monster -= monster # この処理はいらない

print(killed)
