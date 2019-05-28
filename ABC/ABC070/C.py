import fractions
from functools import reduce

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def main():
    N = int(input())
    li = []
    for i in range(N):
        li.append(int(input()))
    
    print(lcm_list(li))

main()