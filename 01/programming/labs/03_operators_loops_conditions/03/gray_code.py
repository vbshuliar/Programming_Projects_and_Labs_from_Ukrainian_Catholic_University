num1 = "0b" + str(input())

num2 = int(num1, 2)
num3 = num2 >> 1
gray = num2 ^ num3
result = bin(gray)[2:]

while (len(num1)) - 2 > len(result):
	result = "0" + result

print(result)