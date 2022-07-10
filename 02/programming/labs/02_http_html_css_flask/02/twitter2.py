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


def friends():
    """Grabs all required information."""
    print("\nEnter Twitter Account:\n")
    acct = input('>>>')
    if len(acct) < 1:
        return
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '10'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    return js


if __name__ == "__main__":
    print(friends())
