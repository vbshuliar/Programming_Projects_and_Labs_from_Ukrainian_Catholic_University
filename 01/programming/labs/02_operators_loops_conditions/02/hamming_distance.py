c = input().split()
a = int(c[0])
b = int(c[1])
d = a ^ b
counter = 0
for i in range(d):		
	if (d >> i) & 1 != 0:
		counter += 1
print(counter)
