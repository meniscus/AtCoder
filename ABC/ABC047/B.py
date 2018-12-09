import collections as cl

W,H,N = [int(i) for i in input().split()]
action_list = []
ACTION_INDEX = {
	"X" : 0,
	"Y" : 1,
	"TYPE" : 2
}
ACTION_TYPE = {
	"LESS_THAN_X" : 1,
	"MORE_THAN_X" : 2,
	"LESS_THAN_Y" : 3,
	"MORE_THAN_Y" : 4,
}

for i in range(N) :
	action_list.append([int(i) for i in input().split()])

arr = [[0 for i in range(H)] for j in range(W)]

for actions in action_list :
	if(actions[ACTION_INDEX["TYPE"]] == ACTION_TYPE["LESS_THAN_X"]) :
		for i in range(actions[ACTION_INDEX["X"]]) :
			for j in range(H) :
				arr[i][j] = 1

	elif (actions[ACTION_INDEX["TYPE"]] == ACTION_TYPE["MORE_THAN_X"]) :
		for i in range(actions[ACTION_INDEX["X"]], W) :
			for j in range(H) :
				arr[i][j] = 1
	elif (actions[ACTION_INDEX["TYPE"]] == ACTION_TYPE["LESS_THAN_Y"]) :
		for i in range(W) :
			for j in range(actions[ACTION_INDEX["Y"]]) :
				arr[i][j] = 1
	elif (actions[ACTION_INDEX["TYPE"]] == ACTION_TYPE["MORE_THAN_Y"]) :
		for i in range(W) :
			for j in range(actions[ACTION_INDEX["Y"]], H) :
				arr[i][j] = 1

arr2 = []
for i in range(W) :
	for j in range(H) :
		arr2.append(arr[i][j])
c = cl.Counter(arr2)
print(c[0])