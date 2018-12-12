H,W = [int(i) for i in input().split()]
pictures = ["#" * (W+2)]
for i in range(H) :
    pictures.append("#" + input() + "#")

pictures.append("#" * (W+2))

for picture in pictures :
    print(picture)