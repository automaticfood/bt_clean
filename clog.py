#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('/www/server/panel/data/default.db')
c = conn.cursor()

c.execute("DELETE from logs;")
conn.commit()
print ("Total number of rows deleted :", conn.total_changes)

conn.close()