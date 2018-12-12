import collections

S = list(input())
c = collections.Counter(S)
if (c.most_common()[0][1] != 1) :
    print("no")
else :
    print("yes")

