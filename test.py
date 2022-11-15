import sqlite3
import datetime
from datetime import datetime

conn = sqlite3.connect('test.db')

print("Opened database successfully")

c = conn.cursor()

# create


# def add(id, message, status, startDate):
#     data_tuple = (id, message, status, startDate)
#     sqlite_insert_with_param = """INSERT INTO 'main'
#                           ('id', 'message', 'status', 'started_at')
#                           VALUES (?, ?, ?, ?);"""
#     c.execute(sqlite_insert_with_param, data_tuple)


# add(1, 'Hello', 'running', datetime.datetime.now())

# list
# c.execute("SELECT * FROM main")

# print(c.fetchall())

# update
# def update(message, id):
#     date_tuple = (message, id)
#     sqlite_update_with_param = ''' UPDATE main
#               SET message = ?
#               WHERE id = ?'''
#     c.execute(sqlite_update_with_param, date_tuple)


# update('updated hello', 1)

# delete
# def delete(id):
#     data_tuple = (id,)
#     sqlite_delete_with_param = "DELETE from main where id = ?"
#     c.execute(sqlite_delete_with_param, data_tuple)


# delete(1)

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


stop(1)


conn.commit()

conn.close()
