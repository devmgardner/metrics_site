import sqlite3 as sq
from datetime import datetime
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

dbname = os.path.join(currentdir, 'Ergo-API.sqlite')
dbcon = sq.connect(dbname)
dbcur = dbcon.cursor()
datelist = dbcur.execute('SELECT * FROM data').fetchall()
polltimelist = [i[11] for i in datelist]
#for time in polltimelist:
#    row = dbcur.execute('SELECT * FROM data WHERE polltime = ?', (time,)).fetchone()
#    newdate = int(datetime.strptime(time, '%m-%d-%Y %H:%M:%S %Z').timestamp())
#    dbcur.execute('UPDATE data SET polltime = ? WHERE polltime = ?;', (newdate, time,))
for i in datelist:
    try:
        int(i[11])
    except:
        print(i[11])
        #print(int(datetime.strptime(i[11], '%m-%d-%Y %H:%M:%S %Z').timestamp()))
        existingdate = i[11]
        newdate = int(datetime.strptime(i[11], '%m-%d-%Y %H:%M:%S %Z').timestamp())
        print(f'newdate is {newdate}')
        updatecommand = 'UPDATE data SET polltime=? WHERE polltime=?'
        updatedata = (newdate, i[11])
        dbcur.execute(updatecommand, updatedata)
        dbcon.commit()