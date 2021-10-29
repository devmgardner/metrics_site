import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
#
import sqlite3 as sq
ergodb = sq.connect(f'{currentdir}\Alinthar-API.sqlite')
ergocon = ergodb.cursor()
ergocon.execute('''CREATE TABLE "data" (
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
	"skills"	TEXT,
	PRIMARY KEY("polltime")
);''')