import math


def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)


def bruteForce(points):
    p1 = []
    p2 = []
    md = 10**9
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            td = dist(points[i], points[j])
            if(td < md):
                p1, p2 = points[i], points[j]
                md = td
    return (p1, p2, md)


def rec(xsorted, ysorted):
    n = len(xsorted)
    if(n <= 3):
        return bruteForce(xsorted)
    else:
        mid = xsorted[n//2]
        xsl = xsorted[:n//2]
        xsr = xsorted[n//2:]
        ysl = []
        ysr = []
        for p in ysorted:
            ysl.append(p) if p[1] < mid[1] else ysr.append(p)
        (pl1, pl2, dl) = rec(xsl, ysl)
        (pr1, pr2, dr) = rec(xsr, ysr)
        (p1, p2, md) = (pl1, pl2, dl) if dl < dr else (pr1, pr2, dr)
        strip = [p for p in ysorted if(mid[0]-md < p[0] and p[0] < mid[0]+md)]
        for i in range(len(strip)):
            for j in range(i+1, min(i+7, len(strip))):
                td = dist(strip[i], strip[j])
                if(td < md):
                    (p1, p2, md) = (strip[i], strip[j], td)
        return (p1, p2, md)


def minDist(points):
    xsorted = sorted(points, key=lambda x: x[0])
    ysorted = sorted(points, key=lambda x: x[1])
    return rec(xsorted, ysorted)


points = [[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]
p1, p2, md = minDist(points)
print(p1, p2, md)
