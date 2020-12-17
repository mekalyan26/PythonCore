# Method 1 Area of a circle with lists
import math
def area(r):    
    return math.pi * (r**2)
radii = [1,3.3,0.5,7,10]
areas =[]
for r in radii:
    a = area(r)
    areas.append(a)
print(areas)

#Method 2 Area of circle with Map function
print(list(map(area,radii)))

