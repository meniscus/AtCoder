import sys

def print_array_to_line(array) :
	for s in array:
		print(s)


data_count = int(input())
args = [input() for i in range(data_count)]

timespan_list = list(set(args))
timespan_list.sort()

if len(timespan_list) == 1 :
	print_array_to_line(timespan_list)
	sys.exit()

startTime = timespan_list[0].split("-")[0]
endTime = timespan_list[0].split("-")[1]
result_list = []
added = False

for s in timespan_list:
	separated = s.split("-")
	if added == True :
		startTime = separated[0]
		endTime = separated[1]
	
	if separated[0] <= endTime and separated[1] > endTime :
		result_list.append(startTime + "-" + separated[1]);
		timespan_list.remove(s)
		added=True


print(result_list)