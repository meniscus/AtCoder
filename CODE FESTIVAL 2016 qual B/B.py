N,A,B = [int(i) for i in input().split()]
S = input()

all_passed = 0
foreign_passed = 0
for s in S :
    if (s == 'a' and all_passed < A+B) :
        all_passed += 1
        print("Yes")
        continue
    
    if (s == 'b' and all_passed < A+B and foreign_passed < B) :
        all_passed += 1
        foreign_passed += 1
        print("Yes")
        continue
    
    print("No")
