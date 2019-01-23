gp1 = [1,3,5,7,8,10,12]
gp2 = [4,6,9,11]
gp3 = [2]
x,y = [int(i) for i in input().split()]

if ((x in gp1 and y in gp1) or (x in gp2 and y in gp2) or(x in gp3 and y in gp3)) :
    print("Yes")
else :
    print("No")