import urllib.request
import urllib.parse
import urllib.error
import ssl
import pprint
import requests
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def tweets():
    """Grabs all tweets."""
    print("\nEnter Twitter Account:\n")
    acct = input('>>>')
    if len(acct) < 1:
        return
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'})
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(tweets())
