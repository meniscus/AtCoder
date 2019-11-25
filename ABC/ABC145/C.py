import statistics
import itertools
import math

def get_distance(from_x, from_y, to_x, to_y) :
    return math.sqrt((to_x-from_x) **2 + (to_y-from_y)**2)

def main() :
    N = int(input())
    dic = {}
    for i in range(N) :
        p = input().split()
        dic[i] = {"x":int(p[0]), "y":int(p[1])}
    
    town_list = [int(i) for i in range(N)]

    route_list = list(itertools.permutations(town_list,N))

    total_distance = 0
    for routes in route_list :
        for i in range(len(routes)-1) :
            current_town = dic[routes[i]]
            next_town = dic[routes[i+1]]
            total_distance += get_distance(current_town["x"], current_town["y"], next_town["x"], next_town["y"])
    
    # print(total_distance / N)
    print(total_distance / math.factorial(N))


main()