meter=int(input())
kilometer = meter / 1000.0

if meter < 100 :
	ans=00
elif meter <= 5000 :
	ans = kilometer * 10
elif meter <= 30000:
	ans = kilometer + 50
elif meter <= 70000:
	ans = int((kilometer-30) //5 + 80)
else :
	ans=89

s = '%02d' % ans
s = s[0:2]
print(s)
