import math

r = float(input())
h = float(input())

V = h * math.pi * r**2
A = h * 2 * math.pi * r + 2 * math.pi * r**2

print ('V = ', round(V, 3))
print ('A = ', round(A, 3))