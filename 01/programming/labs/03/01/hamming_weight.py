power = int(input())
num1 = (5**power)
counter = 0
for i in range(num1):
    if (num1 >> i) & 1 != 0:
        counter += 1
answer = "odious" if counter % 2 else "evil"
print(f"Number {num1} is {answer} number. Its hamming weight is {counter}.")
