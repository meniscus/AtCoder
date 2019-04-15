import math

N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

# 最小輸送能力に依存するので。。。？
minimum = min([A,B,C,D,E])

print(math.ceil(N / minimum) + 4)