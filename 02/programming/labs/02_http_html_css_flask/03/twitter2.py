"""Grabs all the required information."""
import urllib.request
import urllib.parse
import urllib.error
import json
import ssl
import twurl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def friends(acct):
    """Grabs all required information."""
    if len(acct) < 1:
        return
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    with open("followings.json", 'w', encoding="UTF-8") as doc:
        json.dump(js, doc, indent=2)
