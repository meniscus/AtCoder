A,B,C = [int(i) for i in input().split()]
# a = A % B
# if (C % a == 0) :
#     print("YES")
# else :
#     print("NO")

msg = "NO"
for a in range(1,100) :
    if ((a*A) % B ==C ):
        msg = "YES"
        break

print(msg)