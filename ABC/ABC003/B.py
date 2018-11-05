
replacable = ['a','t','c','o','d','e','r']

deck1 = input()
deck2 = input()

canWin = True
for i in range(len(deck1)) :
	if (deck1[i] == deck2[i]) :
		continue

	if (deck1[i] == '@' and replacable.count(deck2[i]) != 0) :
		continue
	
	if (deck2[i] == '@' and replacable.count(deck1[i]) != 0) :
		continue
	
	canWin = False
	break


if (canWin == True) :
	print("You can win")
else :
	print("You will lose")
