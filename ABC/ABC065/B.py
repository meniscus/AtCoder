N = int(input())
buttons = []
for i in range(N) :
    buttons.append(int(input()))

push_index = 1
push_count = -1
count = 0
for i in range(N) :
    push_index = buttons[push_index-1]
    count += 1
    if (push_index == 2) :
        push_count = count
        break

print(push_count)