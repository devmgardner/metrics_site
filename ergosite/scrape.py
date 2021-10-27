import xml.etree.ElementTree as ET, sqlite3 as sq, re, requests as rq
import time
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
fname = f'{currentdir}\ergoscrape-log.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')


ergocon = sq.connect(f'{currentdir}\ergo.sqlite')
ergocur = ergocon.cursor()


url = 'https://secure.runescape.com/m=adventurers-log/rssfeed?searchName=Ergo'
response = rq.get(url)
date = time.asctime(time.gmtime())
data = ET.fromstring(response.text)
feed = data[0].findall('item')
for item in feed:
    try:
        title = item.find('title').text
    except:
        fhand.write(f'Error finding item title at time: {time.asctime(time.gmtime())}.\n')
        continue
    try:
        description = re.sub('\t','',re.sub('\n','',item.find('description').text))
    except:
        fhand.write(f'Error finding item description at time: {time.asctime(time.gmtime())}.\n')
        continue
    try:
        link = item.find('link').text
    except:
        fhand.write(f'Error finding item link at time: {time.asctime(time.gmtime())}.\n')
        continue
    #try:
    #    date = item.find('pubDate').text
    #except:
    #    fhand.write(f'Error finding item date at time: {time.asctime(time.gmtime())}.\n')
    #    continue
    try:
        itemid = re.match('.*[&id=-](?P<id>\d*)',item.find('link').text).group('id')
    except:
        fhand.write(f'Error finding item id at time: {time.asctime(time.gmtime())}.\n')
        continue
    if len(ergocur.execute('SELECT * FROM Events WHERE itemid = ?', (itemid,)).fetchall()) == 0:
        ergocur.execute('INSERT INTO Events (itemid, title, description, link, date) VALUES (?, ?, ?, ?, ?)', (itemid, title, description, link, date,))
        ergocon.commit()
    else:
        fhand.write(f'Item {id} already exists in database, skipping.\n')
        continue