import collections as cole

N = int(input())
C_list = list(input())

c = cole.Counter(C_list)
com = c.most_common()
max = com[0][1]
min = 0
if (C_list.count("1") > -1 and C_list.count("2") > 0 and C_list.count("3") > 0 and C_list.count("4") > 0) :
    min = com[-1][1]   
else :
    min = 0
    

print(str(max) + " " + str(min))