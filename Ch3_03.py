# (Geography: estimate areas) Find the GPS locations for Atlanta, Georgia;
# Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina from
# www.gps-data-team.com/map/ and compute the estimated area enclosed by these
# four cities. (Hint: Use the formula in Programming Exercise 3.2 to compute the
# distance between two cities. Divide the polygon into two triangles and use the formula
# in Programming Exercise
# 2.14 to compute the area of a triangle.)
# 3.2 (Geometry: great circle distance) The great circle distance is the distance between
# two points on the surface of a sphere. Let (x1, y1) and (x2, y2) be the geographical
# latitude and longitude of two points. The great circle distance between the two
# points can be computed using the following formula:
# d = radius * arccos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1-y2))
# The average earth radius is 6,371.01 km.
# Python trigonometric functions use radians. 
# The latitude and longitude degrees in the formula are for north and west.
# Use negative to indicate south and east degrees. Here is a sample run:

import math

xAtlanta, yAtlanta = 33.7489954, -84.3879824 
xOrlando, yOrlando = 28.5383355, -81.37923649999999
xSavannah, ySavannah = 32.0835407, -81.09983419999998
xCharlotte, yCharlotte = 35.2270869,-80.84312669999997

RADIUSOFEARTH = 6371.01

xAtlantaRadians = math.radians(xAtlanta)
yAtlantaRadians = math.radians(yAtlanta)

xOrlandoRadians = math.radians(xOrlando)
yOrlandoRadians = math.radians(yOrlando)

xSavannahRadians = math.radians(xSavannah)
ySavannahRadians = math.radians(ySavannah)

xCharlotteRadians = math.radians(xCharlotte)
yCharlotteRadians = math.radians(yCharlotte)

A1 = RADIUSOFEARTH * (math.acos(math.sin(xAtlantaRadians) * math.sin(xOrlandoRadians) /
        + math.cos(yAtlantaRadians) * math.cos(yOrlandoRadians) * math.cos(yAtlantaRadians - yOrlandoRadians)))

B1 = RADIUSOFEARTH * (math.acos(math.sin(xAtlantaRadians) * math.sin(xSavannahRadians) /
        + math.cos(yAtlantaRadians) * math.cos(ySavannahRadians) * math.cos(yAtlantaRadians - ySavannahRadians)))

C1 = RADIUSOFEARTH * (math.acos(math.sin(xSavannahRadians) * math.sin(xOrlandoRadians) /
        + math.cos(xSavannahRadians) * math.cos(yOrlandoRadians) * math.cos(xSavannahRadians - yOrlandoRadians)))

A2 = RADIUSOFEARTH * (math.acos(math.sin(xAtlantaRadians) * math.sin(xCharlotteRadians) /
        + math.cos(yAtlantaRadians) * math.cos(yCharlotteRadians) * math.cos(yAtlantaRadians - yCharlotteRadians)))

B2 = B1

C2 = RADIUSOFEARTH * (math.acos(math.sin(xCharlotteRadians) * math.sin(xSavannahRadians) /
        + math.cos(yCharlotteRadians) * math.cos(ySavannahRadians) * math.cos(yCharlotteRadians - ySavannahRadians)))

S1 = (A1 + B1 + C1)/2

S2 = (A2 + B2 + C2)/2

area1 = math.sqrt(S1 * (S1 - A1) * (S1 - B1) * (S1 - C1))

area2 = math.sqrt(S2 * (S2 - A2) * (S2 - B2) * (S2 - C2))

totalArea = area1 + area2

print("Estimated area enclosed by the cities of Orlando, Savannah, Charlotte and Atlanta is", 
      format(totalArea,"<10.2f"), "km")