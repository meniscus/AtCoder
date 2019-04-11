N,M = [int(i) for i in input().split()]

list_list = []
for i in range(N) :
    line = input().split()
    del line[0]
    list_list.append(line)

s = set(list_list[0])
for i in range(1,N) :
    s = s & set(list_list[i])

print(len(s))