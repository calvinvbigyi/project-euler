import numpy as np
from datetime import datetime
startTime = datetime.now()

f = open("p102_triangles.txt")

results = 0

def total_area(ts):
	return np.abs(ts[0][0] * (ts[1][1] - ts[2][1]) - ts[0][1] * (ts[1][0] - ts[2][0]) + ts[0][2] * (ts[1][0] * ts[2][1] - ts[1][1] * ts[2][0]))

def splited_area(s):
	return np.abs(s[0][0] * s[1][1] - s[0][1] * s[1][0])

for line in f:
	x1,y1,x2,y2,x3,y3 = [int(i) for i in line.rstrip("\n").split(",")]
	ts = [[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]]
	s1 = [[x1, y1], [x2, y2]]
	s2 = [[x1, y1], [x3, y3]]
	s3 = [[x2, y2], [x3, y3]]
	ta = total_area(ts)
	sa = splited_area(s1) + splited_area(s2) + splited_area(s3)
	if ta == sa:
		results += 1

print(results)
print(datetime.now() - startTime)
