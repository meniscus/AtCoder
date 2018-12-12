N,M = [int(i) for i in input().split()]
student_location = []
for i in range(N) :
    student_location.append([int(i) for i in input().split()])

checkpoint_location = []
for i in range(M) :
    checkpoint_location.append([int(i) for i in input().split()])

for student_loc in student_location :
    min_distance = 9999999999
    min_distance_index = -1
    index = 0
    for checkpoint_loc in checkpoint_location :
        index += 1
        d = abs(student_loc[0] - checkpoint_loc[0]) + abs(student_loc[1] - checkpoint_loc[1])
        if (d < min_distance) :
            min_distance = d
            min_distance_index = index
    # print([d,index])
    print(min_distance_index)
