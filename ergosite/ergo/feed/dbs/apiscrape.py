import os, sys, json, requests as rq, sqlite3 as sq, time, xml.etree.ElementTree as ET, re
from datetime import datetime
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
names = ['Ergo','Alinthar','dasn1u']
for name in names:
    print(name)
    fname = f'{currentdir}/{name}-scrapelog.txt'
    try:
        fhand = open(fname, 'a')
    except FileNotFoundError:
        fhand = open(fname, 'w')
    
    
    apiurl = 'https://apps.runescape.com/runemetrics/profile/profile?user=' + name + '&activities=20'
    apidata = rq.get(apiurl).json()
    dbname = f'{currentdir}/{name}-API.sqlite'
    dbcon = sq.connect(dbname)
    dbcur = dbcon.cursor()
    #insertdata = (apidata['name'], apidata['rank'], apidata['melee'], apidata['combatlevel'], apidata['ranged'], apidata['totalxp'], apidata['questscomplete'], apidata['questsnotstarted'], apidata['questsstarted'], apidata['totalskill'], apidata['magic'], f'{time.strftime("%m-%d-%Y %H:%M:%S",time.gmtime())} UTC', json.dumps(apidata['skillvalues']), json.dumps(apidata['activities']))
    insertdata = (apidata['name'], apidata['rank'], apidata['melee'], apidata['combatlevel'], apidata['ranged'], apidata['totalxp'], apidata['questscomplete'], apidata['questsnotstarted'], apidata['questsstarted'], apidata['totalskill'], apidata['magic'], int(time.time()), json.dumps(apidata['skillvalues']), json.dumps(apidata['activities']))
    insertcommand = 'INSERT INTO data (name, rank, melee, combatlevel, ranged, totalxp, questscomplete, questsnotstarted, questsstarted, totalskill, magic, polltime, skills, activities) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    print(type(apidata['skillvalues']))
    for i in apidata['activities']:
        if len(dbcur.execute('SELECT * FROM activities WHERE date = ? AND details = ? AND text = ?', (i['date'], i['details'], i['text'],)).fetchall()) == 0:
            dbcur.execute('INSERT INTO activities (date, details, text, datetime) VALUES (?, ?, ?, ?)', (i['date'], i['details'], i['text'], int(datetime.strptime(i["date"], "%d-%b-%Y %H:%M").timestamp())))
            dbcon.commit()
    dbcur.execute(insertcommand, insertdata)
    dbcon.commit()
    dbcon.close()



    eventurl = f'https://secure.runescape.com/m=adventurers-log/rssfeed?searchName={name}'
    response = rq.get(eventurl)
    eventdata = ET.fromstring(response.text)
    feed = eventdata[0].findall('item')
    eventdb = f'{currentdir}/{name}.sqlite'
    eventcon = sq.connect(eventdb)
    eventcur = eventcon.cursor()
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
        if len(eventcur.execute('SELECT * FROM Events WHERE itemid = ?', (itemid,)).fetchall()) == 0:
            eventcur.execute('INSERT INTO Events (itemid, title, description, link, date) VALUES (?, ?, ?, ?, ?)', (itemid, title, description, link, date,))
            eventcon.commit()
        else:
            fhand.write(f'{time.strftime("%m-%d-%Y %H:%M:%S",time.gmtime())} UTC - {itemid} dupcheck\n')
            continue