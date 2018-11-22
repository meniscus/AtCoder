import sys
input = sys.stdin.readline
N = int(input())
people = [int(i) for i in input().split()]
desc_list = people[:]
desc_list.sort(reverse=True)

for i in desc_list :
	print(people.index(i) + 1)
