import sqlite3
import datetime


def get_chrome(con: sqlite3.Connection) -> list:
    """
    Reads database of Chrome history and process data
    :param con: database connection
    :return: list of visits
    """
    c = con.cursor()

    c.execute("select id, url, title from urls")
    url_id_tuples = c.fetchall()
    url_id = dict()
    for url in url_id_tuples:
        url_id[url[0]] = (url[1], url[2])

    c.execute("select url, visit_time, visit_duration from visits")
    results_with_url_as_id = c.fetchall()

    results = []
    for result in results_with_url_as_id:
        url = url_id[result[0]]
        date = datetime.datetime.fromtimestamp((result[1]) / 1000000 - 11644473600).__str__().split()
        results.append((url[0], url[1], date[0], date[1], result[2]))

    c.close()
    return results


def get_chrome_os(user: str, os: str) -> list:
    """
    Reads Chrome History on Linux
    Returns list of tuples. Each tuple has structure:
    (url: srt, title: str, date_of_last_visit: str("yyyy-mm-dd"),
    time_of_last_visit: str("hh:mm:ss.ms"), time_of_visit: int)
    :param user: username of computer
    :param os: OS of computer. Can be "Windows", "Linux" or "MacOS"
    :return: list of visits
    """
    if os == "Linux":
        con = sqlite3.connect(f'/home/{user}/.config/google-chrome/Default/History')
    elif os == "Windows":
        con = sqlite3.connect(f'C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History')
    elif os == "MacOS":
        con = sqlite3.connect(f'/Users/{user}/Library/Application Support/Google/Chrome/Default/History')
    else:
        raise ValueError("Incorrect OS")
    return get_chrome(con)


def write_data_to_file(history: list, filename: str) -> None:
    """
    Writes data to file
    :param history: list of visits of browser
    :param filename: name of file to write
    :return:
    """
    with open(filename, "w", encoding="utf-8") as file:
        for element in history:
            file.write(str(element) + "\n")


if __name__ == '__main__':
    # Put here values from your computer
    history = get_chrome_os("admin", "Windows")
    write_data_to_file(history, "history.txt")