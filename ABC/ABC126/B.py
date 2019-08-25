S = input()

head = S[0] + S[1]
tail = S[2] + S[3]

is_head_month = False
is_tail_month = False

if (int(head) <= 12 and int(head) != 0) :
    is_head_month = True

if (int(tail) <= 12 and int(tail) != 0) :
    is_tail_month = True

if (is_head_month == True and is_tail_month == True) :
    print("AMBIGUOUS")
elif (is_head_month == True and is_tail_month == False) :
    print("MMYY")
elif (is_head_month == False and is_tail_month == True) :
    print("YYMM")
else :
    print("NA")