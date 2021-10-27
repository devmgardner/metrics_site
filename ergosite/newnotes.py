import requests as rq, json, os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
playername = input(f'Input player name to search\n> ')
#url = 'https://apps.runescape.com/runemetrics/profile/profile?user=Ergo&activities=20'
url = 'https://apps.runescape.com/runemetrics/profile/profile?user=' + playername + '&activities=20'
data = rq.get(url)
with open(f'{currentdir}\{playername}.txt','w') as fhand:
    json.dump(data.json(), fhand, indent=2)