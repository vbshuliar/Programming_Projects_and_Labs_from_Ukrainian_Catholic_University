"""
olympics data operating
"""


import pandas as pd


def read_data():
    """
    reads data from csv file
    """

    df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
    for col in df.columns:
        if col[:2] == '01':
            df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
        elif col[:2] == '02':
            df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
        elif col[:2] == '03':
            df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
        elif col[:1] == '№':
            df.rename(columns={col: '#' + col[1:]}, inplace=True)

    names_ids = df.index.str.split('\\s\\(')
    df.index = names_ids.str[0]
    df['ID'] = names_ids.str[1].str[:3]
    df = df.drop('Totals')

    return df


def first_country(df):
    """
    returns first country

    >>> first_country(pd.DataFrame([[1, 2, 3, 4, 5, 6], \
[7, 8, 9, 10, 11, 12]], columns=['Gold', \
'Gold.1', 'Silver', 'Silver.1', 'Bronze', \
'Bronze.1'], index=['Ukraine', 'Poland']))
    Gold        1
    Gold.1      2
    Silver      3
    Silver.1    4
    Bronze      5
    Bronze.1    6
    Name: Ukraine, dtype: int64
    """

    return df.head(1).squeeze()


def summer_biggest(df):
    """
    returns country with the biggest amount of gold medals"

    >>> summer_biggest(pd.DataFrame([[1, 2, 3, 4, 5, 6], \
[7, 8, 9, 10, 11, 12]], columns=['Gold', \
'Gold.1', 'Silver', 'Silver.1', 'Bronze', \
'Bronze.1'], index=['Ukraine', 'Poland']))
    'Poland'
    """

    return df.sort_values(by=['Gold'], ascending=False).index[0]


def difference_biggest(df):
    """
    returns sorted df with difference

    >>> difference_biggest(pd.DataFrame([[1, 2, 3, 4, 5, 6], \
[7, 8, 9, 10, 11, 12]], columns=['Gold', \
'Gold.1', 'Silver', 'Silver.1', 'Bronze', \
'Bronze.1'], index=['Ukraine', 'Poland']))
    'Ukraine'
    """

    df["module"] = abs(df["Gold"] - df["Gold.1"])
    df = df.sort_values(by=["module"], ascending=False)
    df.pop("module")

    return df.index[0]


def difference_biggest_relative(df):
    """
    returns difference

    >>> difference_biggest_relative(pd.DataFrame([[1, 2, 3, 4, 5, 6], \
[7, 8, 9, 10, 11, 12]], columns=['Gold', \
'Gold.1', 'Silver', 'Silver.1', 'Bronze', \
'Bronze.1'], index=['Ukraine', 'Poland']))
    'Ukraine'
    """

    df["module"] = (abs(df["Gold"] - df["Gold.1"])) / \
        (df["Gold"] + df["Gold.1"])
    df = df[df['module'] != 1]
    df = df.sort_values(by=["module"], ascending=False)
    del df['module']

    return df.index[0]


def get_points(df):
    """
    return points

    >>> get_points(pd.DataFrame([[1, 2, 3, 4, 5, 6], \
[7, 8, 9, 10, 11, 12]], columns=['Gold', \
'Gold.1', 'Silver', 'Silver.1', 'Bronze', \
'Bronze.1'], index=['Ukraine', 'Poland']))
    Ukraine     34
    Poland     106
    Name: Points, dtype: int64
    """

    df['Points'] = ((df['Gold'] + df['Gold.1']) * 3 + (df['Silver'] +
                    df['Silver.1']) * 2 + (df['Bronze'] + df['Bronze.1']))

    return df['Points']


if __name__ == "__main__":
    import doctest
    doctest.testmod()
