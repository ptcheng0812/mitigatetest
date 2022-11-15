import sys
import sqlite3
import datetime
import random
from datetime import datetime

conn = sqlite3.connect('test.db')

print("Opened database successfully")

c = conn.cursor()

if sys.argv[1] == 'list':
    c.execute("SELECT * FROM main")

    print(c.fetchall())

if sys.argv[1] == 'create':
    def add(id, message, status, startDate):
        data_tuple = (id, message, status, startDate)
        sqlite_insert_with_param = """INSERT INTO 'main'
                              ('id', 'message', 'status', 'started_at')
                              VALUES (?, ?, ?, ?);"""
        c.execute(sqlite_insert_with_param, data_tuple)

    n = random.randint(0, 100)
    add(n, sys.argv[2], 'running', datetime.now())

if sys.argv[1] == 'update':
    def update(message, id):
        date_tuple = (message, id)
        sqlite_update_with_param = ''' UPDATE main
                                      SET message = ?
                                      WHERE id = ?'''
        c.execute(sqlite_update_with_param, date_tuple)

    update(sys.argv[3], sys.argv[2])

if sys.argv[1] == 'delete':
    def delete(id):
        data_tuple = (id,)
        sqlite_delete_with_param = "DELETE from main where id = ?"
        c.execute(sqlite_delete_with_param, data_tuple)

    delete(sys.argv[2])

if sys.argv[1] == 'stop':
    def stop(id):
        data_tuple = ("stopped", datetime.now(), id)
        sqlite_stop_with_param = ''' UPDATE main
                                SET status = ?,
                                    stopped_at = ?
                                WHERE id = ?'''
        c.execute(sqlite_stop_with_param, data_tuple)

        c.execute("SELECT * FROM main WHERE id=?", (id,))

        rows = c.fetchall()

        for row in rows:
            print(row)
            print("Duration: ", datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S.%f') -
                  datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f'))

    stop(sys.argv[2])

conn.commit()

conn.close()
