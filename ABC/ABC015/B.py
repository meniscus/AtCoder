import math
# あ
software_count = int(input())
bug_list = []
bug_total = 0
bug_software = 0
for bug in input().split() :
	if (int(bug) > 0 ) :
		bug_total += int(bug)
		bug_software += 1

print(math.ceil(bug_total / bug_software))