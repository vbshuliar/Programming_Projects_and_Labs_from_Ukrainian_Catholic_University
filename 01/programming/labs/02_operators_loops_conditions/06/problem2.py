side = int(input())
for n in range(side):
	if (n <= 1) or (n == (side-1)):
		print("*"*(n + 1))
	else:
		print("*"+(" "*(n-1))+"*")