A,B = map(int,input().split())

m = A+B
if (m < A-B) :
    m = A-B

if (m < A*B) :
    m = A*B

print(m)