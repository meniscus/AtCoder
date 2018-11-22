N = int(input())
people = {int(j):int(i) for i,j in enumerate(input().split())}
people = sorted(people.items(), key=lambda x: x[0], reverse=True)
for k,v in people :
	print(v+1)
