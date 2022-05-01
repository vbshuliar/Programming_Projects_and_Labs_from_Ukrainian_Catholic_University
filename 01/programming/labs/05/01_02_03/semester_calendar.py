import calendar


def semester_calendar(output_type, year, first_month, last_month):
    """returns semester calendar
    >>> semester_calendar("txt", 2021, 10, 10)
    '    October 2021\\nMo Tu We Th Fr Sa Su\\n       \
      1  2  3\\n 4  5  6  7 \
 8  9 10\\n11 12 13 14 15 16 17\\n18 19 20 21 22 \
23 24\\n25 26 27 28 29 30 31\\n'
    """
    kalendar = ""
    months = last_month - first_month + 1
    if output_type == "html":
        kalendar_HTML = calendar.HTMLCalendar(0)
        for i in range(months):
            kalendar = kalendar + \
                kalendar_HTML.formatmonth(year, first_month + i)
    elif output_type == "txt":
        for i in range(months):
            kalendar = kalendar + calendar.month(year, first_month + i)
    else:
        return None
    return kalendar