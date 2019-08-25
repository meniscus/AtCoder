N = int(input())
S = input()

# print(S.count("#."))


# 最後の.から前の#は置き換える、でいいはず
first_black = S.find("#")
if (first_black == -1) :
    first_black = 0

last_white = S.rfind(".")
if (last_white == -1) :
    last_white = N-1

S2 = S[first_black:last_white+1]
b_to_w = S2.count("#")
w_to_b = S2.count(".")
print(min(b_to_w,w_to_b))
    