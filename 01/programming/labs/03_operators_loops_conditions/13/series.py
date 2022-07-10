n = int(input())
a = 1
b = 2
for i in range(n):
	if i == n - 1:
		print(f"{a}/{a+1}")
	elif i < n - 1 and b % 2 == 0:
		print(f"{a}/{a+1}", end = " ")
		print("-", end = " ")
	elif i < n - 1 and b % 2 != 0:
		print(f"{a}/{a+1}", end = " ")
		print("+", end = " ")	
	b += 1
	a += 2