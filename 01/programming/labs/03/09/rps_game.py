a = list(str(input()))
while (True):
    b = input()
    a += b
    if b == "":
        break
for n in range(int(len(a)/2)):
	
	if (a[2*n] == "R" and a[2*n+1] == "S") or (a[2*n] == "S" and a[2*n+1] == "P")\
or (a[2*n] == "P" and a[2*n+1] == "R"):
		print("True")
		
	if (a[2*n] == "S" and a[2*n+1] == "R") or (a[2*n] == "P" and a[2*n+1] == "S")\
or (a[2*n] == "R" and a[2*n+1] == "P"):
		print("False")
		
	if (a[2*n] == "S" and a[2*n+1] == "S") or (a[2*n] == "P" and a[2*n+1] == "P")\
or (a[2*n] == "R" and a[2*n+1] == "R"):
		print("False | False")
		