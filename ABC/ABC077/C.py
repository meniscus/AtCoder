import bisect as bis

def main() :
	N = int(input())
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]
	c = [int(i) for i in input().split()]

	a.sort()
	b.sort()
	c.sort()

	count = 0
	for i in b :
		n = bis.bisect_left(a,i)
		m = len(c) - bis.bisect_right(c,i)
		count += n*m

	print(count)

main()