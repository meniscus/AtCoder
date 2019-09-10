N = int(input())
A_list = [int(i) for i in input().split()]
B_list = [int(i) for i in input().split()]
C_list = [int(i) for i in input().split()]

satisfying = 0
prev_dish = A_list[0]
for i in range(N) :
    current_dish = A_list[i]
    satisfying += B_list[current_dish-1]
    # print("get", B_list[current_dish-1])

    if (prev_dish + 1 == current_dish) :
        satisfying += C_list[current_dish-2]
        # print("additional get",C_list[current_dish-2])

    prev_dish = current_dish

print(satisfying)