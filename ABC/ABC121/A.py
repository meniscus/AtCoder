H,W = [int(i) for i in input().split()]
h,w = [int(i) for i in input().split()]

black = (h * W + w * H) - (h * w)
print (H * W - black)