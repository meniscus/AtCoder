# あ
elapsed_second = int(input())

h = int(elapsed_second / 3600)
m = int(elapsed_second % 3600 / 60 )
s = int(elapsed_second % 3600 % 60)

print(str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2))