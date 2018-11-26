import math
def rotation(x1,y1,x2,y2) :
	rot_rad = math.radians(270)
	
	x3 = (x2-x1) * math.cos(rot_rad) - (y2-y1) * math.sin(rot_rad) + x1
	y3 = (x2-x1) * math.sin(rot_rad) + (y2-y1) * math.cos(rot_rad) + y1
	
	return {"x":x3, "y":y3}

x1,y1,x2,y2 = [int(i) for i in input().split()]
rotated = rotation(x2,y2,x1,y1)
x3 = rotated["x"]
y3 = rotated["y"]
rotated = rotation(x3,y3,x2,y2)
x4 = rotated["x"]
y4 = rotated["y"]

print(str(round(x3)) + " " + str(round(y3)) + " " + str(round(x4)) + " " + str(round(y4)))