import itertools as it

def main() :
    start_temp, end_temp = [int(i) for i in input().split()]
    actions = [-10,-5,-1,1,5,10]

    if (start_temp == end_temp) :
        print(0)
        return
    
    needle = abs(end_temp - start_temp)
    for i in range(1, 10) :
        combi = list(it.combinations_with_replacement(actions, i))
        for s in combi :
            if (sum(s) == needle) :
                print(i)
                return
    





main()