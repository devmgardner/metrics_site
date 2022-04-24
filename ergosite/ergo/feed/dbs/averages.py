import sqlite3 as sq
import requests as rq
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
players = ['Ergo','Alinthar','Naevyse','Alrick35']

def xpaverages(player):
    averagelist = []
    url = 'https://apps.runescape.com/runemetrics/xp-monthly?searchName={x}&skillid={y}'
    for i in range(28):
        try:
            data = rq.get(url.format(x=player, y=str(i)))
            averagexpgain = data.json()['monthlyXpGain'][0]['averageXpGain']
            totalgain = data.json()['monthlyXpGain'][0]['totalGain']
            lastmonthgain = data.json()['monthlyXpGain'][0]['monthData'][11]['xpGain']
            averagelist.append((i,f'{averagexpgain:,}',f'{totalgain:,}',f'{lastmonthgain:,}'))
        except IndexError:
            averagexpgain = 0
            totalgain = 0
            lastmonthgain = 0
            averagelist.append((i,f'{averagexpgain:,}',f'{totalgain:,}',f'{lastmonthgain:,}'))
    return averagelist

for player in players:
    averagedb = sq.connect(f'{currentdir}/{player}-averages.sqlite')
    averagecur = averagedb.cursor()
    averagecur.execute('''CREATE TABLE IF NOT EXISTS "Averages" (
    "id" INTEGER PRIMARY KEY NOT NULL,
	"skillid"	INT,
	"averagexpgain"	VARCHAR,
	"totalgain"	VARCHAR,
	"lastmonthgain"	VARCHAR
    );''')
    data = xpaverages(player)
    for i in range(28):
        averagecur.execute('INSERT INTO Averages (skillid, averagexpgain, totalgain, lastmonthgain) VALUES (?, ?, ?, ?)', (data[i][0],data[i][1],data[i][2],data[i][3]))
        averagedb.commit()
    averagedb.close()