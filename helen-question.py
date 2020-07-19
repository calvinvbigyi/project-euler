import math

a = 649
b = 0

while a < 100000000:
	while b < a:
		if (math.pow(a, 2) - 1) == 13 * math.pow(b, 2):
			print("result", a, b)
			break
		b += 1
	a += 1
	b = 180