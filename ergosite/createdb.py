import sqlite3 as sq
ergodb = sq.connect('ergo.sqlite')
ergocon = ergodb.cursor()
ergocon.execute('CREATE TABLE Events (id INT PRIMARY KEY, title VARCHAR NOT NULL, description VARCHAR NOT NULL, link VARCHAR, date VARCHAR NOT NULL)')