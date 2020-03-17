H,N = map(int,input().split())
skill_list = [int(i) for i in input().split()]

if (sum(skill_list) < H) :
    print("No")
else :
    print("Yes")