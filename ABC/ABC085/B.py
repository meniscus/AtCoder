N = int(input())
mochi = []
for i in range(N) :
    mochi.append(int(input()))

mochi = set(list(mochi))
print(len(mochi))