import itertools as it
def main() :
    N = int(input())
    S_list = [input() for s in range(N)]
    dic_counts = {"M" : 0, "A" : 0, "R" : 0, "C" : 0, "H" : 0}
    li = ["M","A","R","C","H"]
    combi = list(it.combinations(li,3))

    for s in S_list :
        for key in dic_counts.keys() :
            if (s[0] == key) :
                dic_counts[key] += 1

    sum = 0
    for item in combi :
        sum += dic_counts[item[0]] * dic_counts[item[1]] * dic_counts[item[2]]
    
    print(sum)


main()

# memo
# M1 A1 R1 C1
# M2       C2
# M3
# 
# M,A,R -> 3 * 1 * 1
# M,A,C -> 3 * 1 * 2
# A,R,C -> 1 * 1 * 2

