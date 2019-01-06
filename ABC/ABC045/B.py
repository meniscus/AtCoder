def decide_turn(card) :
	return card.upper()

A = list(input())
B = list(input())
C = list(input())

turn = "A"
while True:
	card = ""
	if (turn == "A") :
		if (len(A) == 0) :
			print("A")
			break
		card = A.pop()
		turn = decide_turn(card)
	elif (turn == "B") :
		if (len(B) == 0) :
			print("B")
			break
		card = B.pop()
		turn = decide_turn(card)
	else :
		if (len(C) == 0) :
			print("C")
			break
		card = C.pop()
		turn = decide_turn(card)
