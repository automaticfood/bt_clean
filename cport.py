#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('/www/server/panel/data/default.db')
c = conn.cursor()

c.execute("DELETE FROM firewall WHERE port='20' OR port='21' OR port='7800' OR port='8881' OR port='8888' OR port='39000-40000';")
conn.commit()
print ("Total number of rows deleted :", conn.total_changes)

conn.close()