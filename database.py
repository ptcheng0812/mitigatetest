#!/usr/bin/python

import sys
import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")

c = conn.cursor()


c.execute('''CREATE TABLE main (
            id INTEGER PRIMARY KEY,
            message TEXT NOT NULL,
            status TEXT NOT NULL,
            started_at timestamp,
            stopped_at timestamp);''')


conn.commit()

conn.close()

print("successfully created table")
