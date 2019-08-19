import statistics as stat
import collections as cl

N = int(input())

s_li = []
s_dic = {}
c = 0
for i in range(N) :
    s = ''.join(sorted(list(input())))
    # con = s_li.count(s)
    # if (con >= 1) :
    #     c += con
    # s_li.append(s)
    if (s in s_dic) :
        c += s_dic[s]
        s_dic[s] += 1
    else :
        s_dic[s] = 1

print(c)