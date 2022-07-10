"""module that creates list of students
"""


import urllib.request


def read_input_file(url, number):
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77

    Return list of strings lists from url

    >>> read_input_file('https://raw.githubusercontent.com/anrom\
7/Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. \
В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.',\
 '+', '195.385', '10.60']]
    """
    url = 'https://raw.githubusercontent.com/anrom7/Test_Olya/maste\
r/New%20folder/total.txt'
    students = []
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.strip()
            line = line.decode('utf-8')
            if 'Українська мова та література' in line or 'Середній \
бал документа про освіту' in line or "—	" in line:
                students.append(line)

    data = []
    for i in range(0, len(students), 3):
        s123 = students[i].split('\t')[:-1]
        if students[i+1][-5] == " ":
            s123.append(students[i+1][-4:])
        else:
            s123.append(students[i+1][-5:])
        s123[2] = students[i+2][-1]
        data.append(s123)

    return data[:number]


def write_csv_file(url):
    """creates and writes csv file
    """
    file_to_write = read_input_file(url, 100)
    with open("total.csv", "w") as file1:
        file1.write("№,ПІБ,Д,Заг.бал,С.б.док.осв.")
        for elem in range(len(file_to_write)):
            temp = ",".join(file_to_write[elem]) + "\n"
            file1.write(temp)
