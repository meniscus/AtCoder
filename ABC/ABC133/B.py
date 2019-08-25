import math

def get_distance(point_A, point_B) :
    s = 0
    for i in range(len(point_A)) :
        s += pow(abs(point_A[i] - point_B[i]),2)
    
    return math.sqrt(s)


N,D = [int(i) for i in input().split()]
points = []
for i in range(N) :
    points.append([int(i) for i in input().split()])

count = 0
for i in range(N) :
    for k in range(i,N) :
        if (i == k) :
            continue
        
        d = get_distance(points[i], points[k])
        # print(d)
        if (float.is_integer(d)) :
            count += 1
        
print(count)
