S = input()

# Sから文字を抜いていって、空文字列になればいいはず
# *erとerase*の先頭がぶつかるのでeraserから調べる
# dreamerを巻き込んでもdreamで拾えるので
S = S.replace("eraser", "")
S = S.replace("erase", "")
S = S.replace("dreamer", "")
S = S.replace("dream", "")

if (len(S) == 0) :
    print("YES")
else :
    print("NO")