import math

m = float(input())
v = float(input())
c = 299792458

mr = (m)/((1-((v**2)/(c**2)))**(1/2))	
e = mr*c**2
print (e)