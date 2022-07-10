import calendar


def semester_calendar(year, month):    
    kalendar = calendar.month(year, month)
    kalendar = kalendar.split("\n")
    kalendar.pop(0)
    kalendar.pop(-1)
    
    for num1 in range(len(kalendar)):
        kalendar[num1] = list(kalendar[num1].split(" "))
    for num1 in range(len(kalendar)):
        while "" in kalendar[num1]:
            kalendar[num1].remove("")
        for num2 in range(len(kalendar[num1])):
            if len(kalendar[num1][num2]) == 1:
                kalendar[num1][num2] = " "+kalendar[num1][num2]
    kalendar_vert = kalendar.copy()
    for num1 in range(len(kalendar)):
        for num2 in range(len(kalendar)):
            try:
                kalendar_vert[num1][num2] = kalendar[num2][num1]
            except IndexError:
                kalendar_vert[num1].append(" ")
    for num1 in range(len(kalendar)):
        print(" ".join(kalendar_vert[num1]))

    kalendar_vert = kalendar.copy()
    # for num1 in range(len(kalendar_vert)):
    #     for num2 in range(len(kalendar_vert[num1])):
    #         kalendar_vert[num1][num2] = kalendar[num2][num1]

    for num1 in range(len(kalendar)):
        print(" ".join(kalendar_vert[num1]))
    print(kalendar)

semester_calendar(2021, 11)