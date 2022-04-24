import sqlite3 as sq
player = input(f'input player name to create files for> ')
dbcon = sq.connect(f'{player}-API.sqlite')
dbcur = dbcon.cursor()
dbcur.execute("""CREATE TABLE IF NOT EXISTS "activities" (
	"date"	TEXT,
	"details"	TEXT,
	"text"	TEXT
, "datetime"	INTEGER)""")
dbcur.execute("""CREATE TABLE IF NOT EXISTS "data" (
	"name"	TEXT,
	"rank"	INTEGER,
	"melee"	INTEGER,
	"combatlevel"	INTEGER,
	"ranged"	INTEGER,
	"totalxp"	INTEGER,
	"questscomplete"	INTEGER,
	"questsnotstarted"	INTEGER,
	"questsstarted"	INTEGER,
	"totalskill"	INTEGER,
	"magic"	INTEGER,
	"polltime"	TEXT,
	"skills"	json,
	"activities"	json,
	PRIMARY KEY("polltime")
)""")
dbcon.commit()
dbcon.close()
dbcon = sq.connect(f'{player}.sqlite')
dbcur = dbcon.cursor()
dbcur.execute("""CREATE TABLE IF NOT EXISTS Events (itemid INT PRIMARY KEY, title VARCHAR NOT NULL, description VARCHAR NOT NULL, link VARCHAR, date VARCHAR NOT NULL)""")
dbcon.commit()
dbcon.close()
dbcon = sq.connect(f'{player}-averages.sqlite')
dbcur = dbcon.cursor()
dbcur.execute("""CREATE TABLE IF NOT EXISTS "Averages" (
    "id" INTEGER PRIMARY KEY NOT NULL,
	"skillid"	INT,
	"averagexpgain"	VARCHAR,
	"totalgain"	VARCHAR,
	"lastmonthgain"	VARCHAR
    )""")
dbcon.commit()
dbcon.close()