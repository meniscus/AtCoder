import collections

def main() :
	N = int(input())
	li = [int(i) for i in input().split()]

	c = collections.Counter(li)

	total_count = 0
	for key in c.keys() :
		count = c[key]

		if (count == key) :
			continue
		elif (count > key) :
			total_count += (count - key)
		else  :
			# all remove
			total_count += count

	print(total_count)


main()

