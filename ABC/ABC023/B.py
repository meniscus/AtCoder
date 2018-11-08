# あ
N = int(input())
s = input()

a = "b"

count = 0
while True :
	if (a == s) :
		break

	if ((count + 1 )% 3 == 1) :
		a = "a" + a + "c"
	elif ((count + 1 )% 3 == 2) :
		a = "c" + a + "a" 
	elif ((count + 1 )%3 == 0) :
		a = "b" + a + "b"
	
	if (count > N) :
		count = -1
		break
	
	count += 1


print(count)