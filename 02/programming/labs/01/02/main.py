"""Html page generator."""
import csv
import argparse
from random import uniform
import pandas as pd
import folium
from haversine import haversine
from cachetools import cached, TTLCache
from geopy.geocoders import Nominatim


def main():
    """The main function."""
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=str)
    parser.add_argument("lat", type=float)
    parser.add_argument("lon", type=float)
    parser.add_argument("inplace", type=str)
    args = parser.parse_args()
    generate(parse(args.inplace, args.year), args.lat, args.lon)


def parse(root, year_check):
    """Parses data and writes csv file."""
    with open(root, "r", encoding="UTF-8", errors="ignore") as base:
        with open("places.csv", "w", encoding="UTF-8", newline="") as locs:
            temp = csv.writer(locs, delimiter=",")
            temp.writerow(["movie", "year", "place", "latitude", "longitude"])
            for each in base.readlines()[14:-1]:
                try:
                    year = each.split("\t")[0].split("(")[1][:4]
                    if year != year_check or not year.isdigit():
                        continue
                    place = (
                        each.split("\t")[-2]
                        .strip()
                        .replace(",", "")
                        .replace("'", "")
                        .replace('"', "")
                        if each.split("\t")[-1].startswith("(")
                        else each.split("\t")[-1]
                        .strip()
                        .replace(",", "")
                        .replace("'", "")
                        .replace('"', "")
                    )
                    coords = location(place)
                    if coords is None:
                        continue
                    name = (
                        each.split("\t")[0]
                        .split("(")[0]
                        .strip()
                        .replace(",", "")
                        .replace("'", "")
                        .replace('"', "")
                    )
                    temp.writerow(
                        [
                            name,
                            int(year),
                            place,
                            coords.latitude + uniform(0.1, 0.2),
                            coords.longitude + uniform(0.2, 0.1),
                        ]
                    )
                except ValueError:
                    continue

    return pd.DataFrame(pd.read_csv("places.csv", delimiter=","))


@cached(cache=TTLCache(maxsize=200, ttl=180))
def location(place):
    """
    Evaluates latitude and longitude.
    >>> place = location('Budapest Hungary')
    >>> (place.latitude, place.longitude)
    (47.4979937, 19.0403594)
    """
    geolocator = Nominatim(user_agent="geoapiExercises")
    coords = geolocator.geocode(place)

    return coords


def generate(data, lat, lon):
    """Generates a map."""
    data["distance"] = data.apply(
        lambda row: haversine((row["latitude"], row["longitude"]), (lat, lon)), axis=1
    )
    data = data.sort_values(["distance"], ascending=True)[:10]

    lati, longi, moive_nm = data["latitude"], data["longitude"], data["movie"]
    user_map = folium.Map(location=[lat, lon], zoom_start=10)
    markers = folium.FeatureGroup(name="Movies")
    for latit, longit, moive_nm in zip(lati, longi, moive_nm):
        markers.add_child(
            folium.Marker(location=[latit, longit], popup=moive_nm, icon=folium.Icon())
        )
    markers.add_child(
        folium.Marker(location=[lat, lon], popup="Start point", icon=folium.Icon())
    )

    capitals = pd.DataFrame(pd.read_csv("capitals.csv", delimiter=","))
    c_lati, c_longi, c_name = (
        capitals["Latitude"],
        capitals["Longitude"],
        capitals["Capital"],
    )
    for latit, longit, moive_nm in zip(c_lati, c_longi, c_name):
        markers.add_child(
            folium.Circle(
                radius=500,
                color="red",
                location=[latit, longit],
                fill=True,
                popup=moive_nm,
            )
        )

    user_map.add_child(markers)
    user_map.save("Map.html")

    return "Map was successfully created"


if __name__ == "__main__":
    main()
