import xml.etree.ElementTree as ET, sqlite3 as sq, re, requests as rq
import time
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
fname = f'{currentdir}/alintharscrape-log.txt'
try:
    fhand = open(fname, 'a')
except FileNotFoundError:
    fhand = open(fname, 'w')
ergocon = sq.connect(f'{currentdir}/alinthar.sqlite')
ergocur = ergocon.cursor()


url = 'https://secure.runescape.com/m=adventurers-log/rssfeed?searchName=Alinthar'
response = rq.get(url)
#date = time.asctime(time.gmtime())
data = ET.fromstring(response.text)
feed = data[0].findall('item')
for item in feed:
    try:
        title = item.find('title').text
    except:
        fhand.write(f'{time.strftime("%m-%d-%Y %H:%M:%S",time.gmtime())} UTC - nferr title\n')
        continue
    try:
        description = re.sub('\t','',re.sub('\n','',item.find('description').text))
    except:
        fhand.write(f'{time.strftime("%m-%d-%Y %H:%M:%S",time.gmtime())} UTC - nferr description\n')
        continue
    try:
        link = item.find('link').text
    except:
        fhand.write(f'{time.strftime("%m-%d-%Y %H:%M:%S",time.gmtime())} UTC - nferr link\n')
        continue
    try:
        date = item.find('pubDate').text
    except:
        fhand.write(f'{time.strftime("%m-%d-%Y %H:%M:%S",time.gmtime())} UTC - nferr date\n')
        continue
    try:
        itemid = re.match('.*[&id=-](?P<id>\d*)',item.find('link').text).group('id')
    except:
        fhand.write(f'{time.strftime("%m-%d-%Y %H:%M:%S",time.gmtime())} UTC - nferr itemid\n')
        continue
    if len(ergocur.execute('SELECT * FROM Events WHERE itemid = ?', (itemid,)).fetchall()) == 0:
        ergocur.execute('INSERT INTO Events (itemid, title, description, link, date) VALUES (?, ?, ?, ?, ?)', (itemid, title, description, link, date,))
        ergocon.commit()
    else:
        fhand.write(f'{time.strftime("%m-%d-%Y %H:%M:%S",time.gmtime())} UTC - {itemid} dupcheck\n')
        continue