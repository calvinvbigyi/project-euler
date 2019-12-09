from datetime import datetime
startTime = datetime.now()

def area(p, q, t=(0,0)):
    return (q[1]-p[1]) * (p[0]-t[0]) - (q[0]-p[0]) * (p[1]-t[1]) > 0

def inside(t0, t1, t2):
    return area(t0, t1) == area(t0, t1, t2) and\
            area(t0, t2) == area(t0, t2, t1) and\
            area(t1, t2) == area(t1, t2, t0)

result = 0
with open("p102_triangles.txt") as f:
    for line in f:
        x1,y1,x2,y2,x3,y3 = line.rstrip("\n").split(",")
        result += inside((int(x1),int(y1)), (int(x2),int(y2)), (int(x3),int(y3)))

print(f"Result: {result}")
print(datetime.now() - startTime)
