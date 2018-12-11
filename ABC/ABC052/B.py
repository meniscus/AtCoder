N = int(input())
S = input()
max_value = 0
current_value = 0
for i in range(len(S)) :
    if (S[i] == 'I') :
        current_value += 1
        if (max_value < current_value) :
            max_value = current_value
    else :
        current_value -= 1

print(max_value)