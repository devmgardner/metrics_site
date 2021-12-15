import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
#
import sqlite3 as sq
ergodb = sq.connect(f'{currentdir}/dasn1u.sqlite')
ergocon = ergodb.cursor()
ergocon.execute('''CREATE TABLE "Events" (
	"itemid"	INT,
	"title"	VARCHAR NOT NULL,
	"description"	VARCHAR NOT NULL,
	"link"	VARCHAR,
	"date"	VARCHAR NOT NULL,
	PRIMARY KEY("itemid")
);''')
