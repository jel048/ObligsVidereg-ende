import math
def getConvexHull(points):
    points = placeP0(points)
    H = []
    H.append(points[0])
    t = [points[0], points[1]]
    end = []
    while end != H[0]:
        for i in points:
            if rightOfTheLine(t[0][0], t[0][1], t[1][0], t[1][1], i[0], i[1]):
                t[1] = i
        H.append(t[1])
        end = t[1]
        t[0] = t[1]
        t[1]= H[0]
        
        
        
    
    return H
    
    
    
    

def placeP0(points):
    rightMostIndex = 0
    r_x, r_y = points[0][0], points[0][1]
    for i in range(1, len(points)):
        xx, yy = points[i][0], points[i][1]
        if yy < r_y:
            r_x, r_y = xx, yy
            rightMostIndex = i
        elif yy == r_y and r_x < xx: 
            r_x = xx
            rightMostIndex = i
    points[0], points[rightMostIndex] = points[rightMostIndex], points[0]
    return points
    


def rightOfTheLine(x0, y0, x1, y1, x2, y2):
    check = (x1-x0) * (y2-y0) - (x2 - x0) * (y1 - y0)
    if check < 0:
        return True
    return False

