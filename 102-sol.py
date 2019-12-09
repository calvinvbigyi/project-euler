import numpy as np
from datetime import datetime
startTime = datetime.now()

f = open("p102_triangles.txt")

results = 0

def total_area(npa_t):
	return np.abs(np.linalg.det(npa_t))

def splited_area(npa_1, npa_2, npa_3):
	return np.abs(np.linalg.det(npa_1)) + np.abs(np.linalg.det(npa_2)) + np.abs(np.linalg.det(npa_3))

for l in f:
	a = [int(i) for i in l[:-1].split(",")]
	npa_t = np.array([[a[0], a[1], 1], [a[2], a[3], 1], [a[4], a[5], 1]])
	npa_s_1 = np.array([[0, 0, 1], [a[0], a[1], 1], [a[2], a[3], 1]])
	npa_s_2 = np.array([[0, 0, 1], [a[0], a[1], 1], [a[4], a[5], 1]])
	npa_s_3 = np.array([[0, 0, 1], [a[2], a[3], 1], [a[4], a[5], 1]])
	ta = total_area(npa_t)
	sa = splited_area(npa_s_1, npa_s_2, npa_s_3)
	if np.abs(ta - sa) <= 3:
		results += 1

print(results)
print(datetime.now() - startTime)
