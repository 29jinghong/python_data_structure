import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()
#connect the .sqlite database with a cursor which works like the file handler
# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')
#have gardian for creating the tables and creats 3 table.

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'
#takes in the file and if there is not a file name enterd it will load roster_data_sample.json

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],
# ]

str_data = open(fname).read()
json_data = json.loads(str_data)
#reades the file and turnes it into a json data that can be used

for entry in json_data:
#can only do iteration if its an array or iterable(dict, list).
    name = entry[0]
    title = entry[1]
    number = entry[2]

    print((name, title, number))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ? , ?)''',
        ( user_id, course_id, number) )

    conn.commit()
