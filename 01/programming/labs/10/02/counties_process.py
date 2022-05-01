"""
counties process opearations
"""


import pandas as pd


def read_data(path_to_file):
    """
    converts csv file data to data frame
    """

    d = pd.read_csv(path_to_file)
    df = pd.DataFrame(d)

    return df


def max_counties(df):
    """
    state with the biggest amount of counties

    >>> max_counties(read_data("census.csv"))
    'Texas'
    """

    df = df[(df["SUMLEV"] == 50)]
    counties = df.pivot_table(columns=['STNAME'], aggfunc='size')

    return counties.sort_values(ascending=False).index[0]


def max_difference(df):
    """
    state with max difference

    >>> max_difference(read_data("census.csv"))
    'Harris County'
    """

    df = df[(df["SUMLEV"] == 50)]
    df['diff'] = df.loc[:, 'POPESTIMATE2010':'POPESTIMATE2015'].max(
        axis=1) - df.loc[:, 'POPESTIMATE2010':'POPESTIMATE2015'].min(axis=1)

    return str(df.sort_values(by=['diff'], ascending=False)['CTYNAME'].values[0])


def conditional_counties(df):
    """
    counditional counties

    >>> conditional_counties(read_data("census.csv"))
                STNAME            CTYNAME
    896           Iowa  Washington County
    1419     Minnesota  Washington County
    2345  Pennsylvania  Washington County
    2355  Rhode Island  Washington County
    3163     Wisconsin  Washington County
    """

    df = df[(df["SUMLEV"] == 50) & ((df["REGION"] == 1) | (df["REGION"] == 2))]
    df = df[df["POPESTIMATE2015"] > df["POPESTIMATE2014"]]
    df = df[df["CTYNAME"].str.startswith("Washington")]

    return df.loc[5:, "STNAME":"CTYNAME"]
