import math

def main() :
    N = int(input())
    point_list = []
    for i in range(N) :
        p = input().split()
        point_list.append({"x" : int(p[0]), "y" : int(p[1])})
    
    max_dis = -1.0
    for p1 in point_list :
        for p2 in point_list :
            if (p1 == p2) :
                continue
            
            d = (p2["x"] - p1["x"]) ** 2 + (p2["y"] - p1["y"]) ** 2
            if (max_dis < d) :
                # sqrtとらなくてもいいよね
                max_dis = d

    print(math.sqrt(max_dis))





main()