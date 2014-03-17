"""
To generate randomly spaced points on a sphere
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

print random_sphere_points(1,4)

	