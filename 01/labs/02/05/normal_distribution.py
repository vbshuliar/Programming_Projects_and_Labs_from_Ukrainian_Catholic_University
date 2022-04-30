import math

x = float(input())
u = float(input())
o = float(input())

f = round((1/((2*math.pi*o**2)**0.5))*(math.e**(-(((x-u)**2)/(2*o**2)))), 10)

print (f)