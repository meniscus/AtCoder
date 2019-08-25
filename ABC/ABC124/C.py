def get_next_expect_color(color) :
    if (color == "1") :
        return "0"
    else :
        return "1"

S = input()

must_reversed_count = 0
expect_color = S[0]

must_reversed_count2 = 1 # 最初が反転なので1にする
expect_color2 = get_next_expect_color(S[0])

for i in range(1,len(S)) :
    if (S[i] == expect_color) :
        must_reversed_count += 1
    
    if (S[i] == expect_color2) :
        must_reversed_count2 += 1

    expect_color = get_next_expect_color(expect_color)
    expect_color2 = get_next_expect_color(expect_color2)

# print(must_reversed_count)
# print(must_reversed_count2)
print(min([must_reversed_count,must_reversed_count2]))



