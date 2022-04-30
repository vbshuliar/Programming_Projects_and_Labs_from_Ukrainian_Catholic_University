"""processes analysis of history of the user
"""


def sites_on_date(visits, date):
    """
    Returns set of all urls that have been visited
    on current date
    :param visits: all visits in browser history
    :param date: date in format "yyyy-mm-dd"
    :return: set of url visited on date
    >>> sites_on_date([('https://www.youtube.com/', 'YouTube', '2021-11-08',\
 '10:14:58.375937', 15525778)], "2021-11-09")
    set()
    """
    urls = []
    for i in range(len(visits)):
        if visits[i][2] == date:
            urls.append(visits[i][0])
    return set(urls)


def most_frequent_sites(visits, number):
    """
    Returns set of most frequent sites visited in total
    Return only 'number' of most frequent sites visited
    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites
    >>> most_frequent_sites([('https://www.youtube.com/', 'YouTube', '2021-11-08',\
 '10:14:58.375937', 15525778)], 1)
    {'https://www.youtube.com/'}
    """
    dkt = {}
    if number == 0:
        return set()
    for num1 in range(len(visits)):
        temp_dkt = {visits[num1][0]: 1}
        if visits[num1][0] in dkt.keys():
            temp_key = dkt.get(visits[num1][0])
            temp_key += 1
            temp_dkt = {visits[num1][0]: temp_key}
        dkt.update(temp_dkt)
    dkt = sorted(dkt.keys(), key=lambda num1: dkt[num1])
    return set(dkt[-number:])


def get_url_info(visits, url):
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)
    >>> get_url_info([('https://www.youtube.com/', 'YouTube', '2021-11-08', \
'10:14:58.375937', 15525778)], 'https://www.youtube.com/')
    ('YouTube', '2021-11-08', '10:14:58.375937', 1, 15525778.0)
    """
    if visits == []:
        return ("", "", "", 0, 0)
    num_of_visits = 0
    average_time = 0
    last_visit_date, last_visit_time = "0", "0"
    for num1 in range(len(visits)):
        if url == visits[num1][0]:
            num_of_visits += 1
            average_time += visits[num1][4]
            last_visit_time1 = float("".join((visits[num1][3]).split(":")))
            last_visit_date1 = float("".join((visits[num1][2]).split("-")))
            temp1 = float("".join(last_visit_time.split(":")))
            temp2 = float("".join(last_visit_date.split("-")))
            title = visits[num1][1]
            if last_visit_time1 >= temp1:
                last_visit_time = visits[num1][3]
            if last_visit_date1 >= temp2:
                last_visit_date = visits[num1][2]
    try:
        average_time /= num_of_visits
    except ZeroDivisionError:
        average_time = 0
    try:
        result = tuple([title, last_visit_date, last_visit_time,
                        num_of_visits, average_time])
    except UnboundLocalError:
        return ("", "", "", 0, 0)
    return result
