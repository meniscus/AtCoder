N,K = [int(i) for i in input().split()]

#あえて文字列とする
a_li = [i for i in input().split()]  

a_li.sort(reverse=True)

out_str = ""
for s in a_li :
    out_str += s

print(out_str)