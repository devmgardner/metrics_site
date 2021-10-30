import os, sys, json, requests as rq, sqlite3 as sq, time, xml.etree.ElementTree as ET, re
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
names = ['Ergo','Alinthar']
for name in names:
    fname = os.path.join(currentdir, f'{name}-scrapelog.txt')
    try:
        fhand = open(fname, 'a')
    except FileNotFoundError:
        fhand = open(fname, 'w')
    url = 'https://apps.runescape.com/runemetrics/profile/profile?user=' + name + '&activities=20'
    data = rq.get(url).json()
    dbname = os.path.join(currentdir, f'{name}-API.sqlite')
    dbcon = sq.connect(dbname)
    dbcur = dbcon.cursor()
    insertdata = (data['name'], data['rank'], data['melee'], data['combatlevel'], data['ranged'], data['totalxp'], data['questscomplete'], data['questsnotstarted'], data['questsstarted'], data['totalskill'], data['magic'], f'{time.strftime("%m-%d-%Y %H:%M:%S",time.gmtime())} UTC', json.dumps(data['skillvalues']))
    insertcommand = 'INSERT INTO data (name, rank, melee, combatlevel, ranged, totalxp, questscomplete, questsnotstarted, questsstarted, totalskill, magic, polltime, skills) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    print(type(data['skillvalues']))
    dbcur.execute(insertcommand, insertdata)
    dbcon.commit()
    dbcon.close()
for name in names:
    fname = os.path.join(currentdir, f'{name}-scrapelog.txt')
    try:
        fhand = open(fname, 'a')
    except FileNotFoundError:
        fhand = open(fname, 'w')
    eventdb = os.path.join(currentdir, f'{name}.sqlite')
    dbcon = sq.connect(eventdb)
    dbcur = dbcon.cursor()
    url = f'https://secure.runescape.com/m=adventurers-log/rssfeed?searchName={name}'
    response = rq.get(url)
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
        if len(dbcur.execute('SELECT * FROM Events WHERE itemid = ?', (itemid,)).fetchall()) == 0:
            dbcur.execute('INSERT INTO Events (itemid, title, description, link, date) VALUES (?, ?, ?, ?, ?)', (itemid, title, description, link, date,))
            dbcon.commit()
        else:
            fhand.write(f'{time.strftime("%m-%d-%Y %H:%M:%S",time.gmtime())} UTC - {itemid} dupcheck\n')
            continue