amount = int(input())
amount_reserved =  amount
rows = 0
counter_rows = 1
counteri = 0
while amount_reserved > 0:
    amount_reserved = amount_reserved - counter_rows
    rows += 1
    counter_rows += 1
width = (rows * 2) - 1
for i in range(rows):
    if i != 0:
        print()       
    print(" "*((rows * 2) - i * 2 - 2), end = "")
    for n in range(i + 1):  
        if n >= i:              
            if counteri < amount:     
                print(chr(65 + counteri), end = "")
            else:
                pass
            counteri += 1
        else:
            if counteri < amount:     
                print(chr(65 + counteri), end = " ")
            else:
                pass
            counteri += 1