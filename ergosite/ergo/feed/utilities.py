import xml.etree.ElementTree as ET, sqlite3 as sq, re, requests as rq
import time, json, os, sys

def scrape(u):
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)
    #
    fname = f'{currentdir}\{u}scrape-log.txt'
    try:
        fhand = open(fname, 'a')
    except FileNotFoundError:
        fhand = open(fname, 'w')
    ergocon = sq.connect(f'{currentdir}\{u}.sqlite')
    ergocur = ergocon.cursor()
    url = f'https://secure.runescape.com/m=adventurers-log/rssfeed?searchName={u}'
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


def apiscrape(u):
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)
    #playername = input(f'Input player name to search\n> ')
    #url = 'https://apps.runescape.com/runemetrics/profile/profile?user=Ergo&activities=20'
    #url = 'https://apps.runescape.com/runemetrics/profile/profile?user=' + playername + '&activities=20'
    #######url = 'https://apps.runescape.com/runemetrics/profile/profile?user=' + u + '&activities=20'
    #######data = rq.get(url).json()
    #with open(f'{currentdir}\{u}.txt','w') as fhand:
    #    json.dump(data, fhand, indent=2)
    dbdir = os.path.join(currentdir, 'dbs')
    lvldb = os.path.join(dbdir, f'{u}-API.sqlite')
    lvlcon = sq.connect(lvldb)
    lvlcur = lvlcon.cursor()
    lvldata = lvlcur.execute('SELECT * FROM data ORDER BY polltime DESC').fetchone()
    return [lvldata[3],lvldata[9],lvldata[5],"{:,}".format(int(re.sub(",", "", lvldata[1]))),lvldata[12],lvldata[6],lvldata[8],lvldata[7]]
    #######return [data['combatlevel'], data['totalskill'], data['totalxp'], "{:,}".format(int(re.sub(",", "", data['rank']))), data['skillvalues'], data['questscomplete'], data['questsstarted'], data['questsnotstarted'], lvldata]

def quests(u):
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)
    url = 'https://apps.runescape.com/runemetrics/quests?user=' + u
    data = rq.get(url).json()
    for i in data['quests']:
        if i['status'] == 'STARTED':
            i['status'] = 'Started'
        elif i['status'] == 'COMPLETED':
            i['status'] = 'Completed'
        elif i['status'] == 'NOT_STARTED':
            i['status'] = 'Not Started'
        if i['difficulty'] == 0:
            i['difficulty'] = 'Novice'
        elif i['difficulty'] == 1:
            i['difficulty'] = 'Intermediate'
        elif i['difficulty'] == 2:
            i['difficulty'] = 'Experienced'
        elif i['difficulty'] == 3:
            i['difficulty'] = 'Master'
        elif i['difficulty'] == 4:
            i['difficulty'] = 'Grandmaster'
        elif i['difficulty'] == 5:
            i['difficulty'] = 'Special'
    return data['quests']
    #with open(os.path.join(currentdir, f'{u}-quests.txt'), 'w') as fhand:
    #    json.dump(data, fhand, indent=2)

def dbscrape(u):
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)
    dbdir = os.path.join(currentdir, 'dbs')
    actdb = os.path.join(dbdir, f'{u}-API.sqlite')
    actcon = sq.connect(actdb)
    actcur = actcon.cursor()
    data = actcur.execute('SELECT * FROM activities ORDER BY datetime DESC').fetchall()
    return data

def avgscrape(u):
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)
    dbdir = os.path.join(currentdir, 'dbs')
    avgdb = os.path.join(dbdir, f'{u}-averages.sqlite')
    avgcon = sq.connect(avgdb)
    avgcur = avgcon.cursor()
    data = []
    for i in range(28):
        result = avgcur.execute('SELECT * FROM Averages WHERE skillid = ? ORDER BY id DESC', (i,)).fetchone()
        data.append((result[0],result[1],result[2],result[3]))
    return data