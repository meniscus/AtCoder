N = int(input())
blue_card = []
for i in range(N) :
    blue_card.append(input())
M = int(input())
red_card = []
for i in range(M) :
    red_card.append(input())

max_get = 0
for bc in blue_card :
    gain = blue_card.count(bc)
    loss = red_card.count(bc)
    score = gain - loss
    if (max_get < score) :
        max_get = score

print(max_get)