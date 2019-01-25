n = int(input())
score_list = list(input())

score_sum = 0
for score in score_list :
    if (score == "A") :
        score_sum += 4
    elif (score == "B") :
        score_sum += 3
    elif (score == "C") :
        score_sum += 2
    elif (score == "D") :
        score_sum += 1

print(score_sum / n) 
