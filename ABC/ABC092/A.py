A = int(input())
B = int(input())
C = int(input())
D = int(input())

if (A > B) :
    fare = B
else :
    fare = A

if (C > D) :
    fare += D
else :
    fare += C

print(fare)
