# (Geometry: two circles) Write a program that prompts the user to enter the
# center coordinates and radii of two circles and determines whether the second
# circle is inside the first or overlaps with the first, as shown in Figure
# 4.11. (Hint: circle2 is inside circle1 if the distance between the two centers
# <= | r1 - r2| and circle2 overlaps circle1 if the distance between the two
# centers <= r1 + r2. Test your program to cover all cases.)
# 
# Here are some sample runs:

# Enter circle1's center x-, y-coordinates, and radius: 
# 0.5, 5.1, 13
# Enter circle2's center x-, y-coordinates, and radius: 
# 1, 1.7, 4.5
# circle2 is inside circle1

# Enter circle1's center x-, y-coordinates, and radius: 
# 4.4, 5.7, 5.5
# Enter circle2's center x-, y-coordinates, and radius: 
# 6.7, 3.5, 3
# circle2 overlaps circle1

import math

x1, y1, radius1 = eval(input("Enter circle1's center x-, y-coordinates, and radius:"))

x2, y2, radius2 = eval(input("Enter circle2's center x-, y-coordinates, and radius:"))

distanceBetweenCentres = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

absoluteDifferenceBetweenRadii = abs(radius1 - radius2)

sumOfRadii = radius1 + radius2

result = ''

if distanceBetweenCentres <= absoluteDifferenceBetweenRadii:
    result = "Circle2 is inside circle1"
elif distanceBetweenCentres <=sumOfRadii:
    result = "Circle2 overlaps circle1"
else:
    result = "Circle2 is outside circle1"
    
print(result)