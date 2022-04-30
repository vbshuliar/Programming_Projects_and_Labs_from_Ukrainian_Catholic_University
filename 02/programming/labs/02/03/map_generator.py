"""Twitter followings parsing."""

import json
from random import uniform
import folium
from geopy.geocoders import Nominatim
from cachetools import cached, TTLCache


def parse_json():
    """Parses followings."""
    with open("followings.json", "r", encoding="UTF-8") as doc:
        data = json.load(doc)['users']
        base = {}
        for _ in data:
            coords = locate(_['location'])
            if coords is None:
                continue
            base[_['screen_name']] = [coords.latitude +
                                      uniform(0.1, 0.2),
                                      coords.longitude +
                                      uniform(0.1, 0.2)]
    return base


@cached(cache=TTLCache(maxsize=200, ttl=180))
def locate(place):
    """
    Evaluates latitude and longitude.
    >>> place = location('Budapest Hungary')
    >>> (place.latitude, place.longitude)
    (47.4979937, 19.0403594)
    """
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        coords = geolocator.geocode(place)
        return coords
    except Exception:
        return


def generate_map(data):
    """Generates a map."""
    user_map = folium.Map()
    if len(data) > 0:
        markers = folium.FeatureGroup(name="Followings")
        for _ in data:
            markers.add_child(folium.Marker(location=data[_],
                                            popup=_,
                                            icon=folium.Icon()))
        user_map.add_child(markers)
    return user_map._repr_html_()
