num_start = int(input())
num_size = int(input())
for n in range(num_size):
	for i in range(num_size - n):		
		if i == (num_size - n - 1):
			print(num_start + i)
		else:
			print(num_start + i, end = " ")