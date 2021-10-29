import os, sys, json, requests as rq, sqlite3 as sq, time
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
    insertdata = (data['name'], data['rank'], data['melee'], data['combatlevel'], data['ranged'], data['totalxp'], data['questscomplete'], data['questsnotstarted'], data['questsstarted'], data['totalskill'], data['magic'], f'{time.strftime("%m-%d-%Y %H:%M:%S",time.gmtime())} UTC', data['skillvalues'])
    insertcommand = 'INSERT INTO data (name, rank, melee, combatlevel, ranged, totalxp, questscomplete, questsnotstarted, questsstarted, totalskill, magic, polltime, skills) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    dbcur.execute(insertcommand, insertdata)
    dbcon.commit()
    dbcon.close()