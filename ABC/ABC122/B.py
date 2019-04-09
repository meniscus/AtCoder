S = input()

str_map = []
for c in S :
    if (c in ['A','C','G','T']) :
        str_map.append('o')
    else :
        str_map.append('x')

print(len(max(''.join(str_map).split('x'))))