"""
To generate 'num' points on a sphere of radius 'r'
- Random placement involves randomly chosen points for 'z' and 'phi'
- Regular placement involves chosing points such that there one point per d_area

References:
Deserno, 2004, How to generate equidistributed points on the surface of a sphere
"""

import random
import math

def random_sphere_points(r,num):
	points = []
	for i in range(0,num):
		z =  random.uniform(-r,r) 
		phi = random.uniform(0,2*math.pi)
		x = math.sqrt(r**2 - z**2)*math.cos(phi)
		y = math.sqrt(r**2 - z**2)*math.sin(phi)
		points.append([x,y,z])
	return points

def regular_sphere_points(r,num):
#
#
#
#


points = random_sphere_points(1,1)
print points
#print math.sqrt(blah[0][0]**2 + blah[0][1]**2 + blah[0][2]**2)

	