def get_greatest_common_divisor(n1, n2) :
    # euclidean_algorithm
    if (n2 == 0) :
        return n1
    return get_greatest_common_divisor(n2, n1 % n2)


N, X = [int(i) for i in input().split()]
locations = [int(i) for i in input().split()]

n2 = abs(locations[0] - X)
for i in range(len(locations),1,-1) :
    n1 = abs(locations[i-1] - X)
    n2 = get_greatest_common_divisor(n1,n2)

print(n2)
# locationsの最大公約数が分かればいいはず。