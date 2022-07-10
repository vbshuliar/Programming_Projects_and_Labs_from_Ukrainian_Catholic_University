n = int(input())
sum = 0
for k in range(n):
	if ((k+1) % 7) == 0:
		sum = sum + (k+1)
	else:
		k += 1
print(sum)