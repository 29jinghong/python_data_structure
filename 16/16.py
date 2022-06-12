import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
# creats a file named emaildb to store the data

cur = conn.cursor()
#you send the sqlite commands throw this cursor and get the respownd throw this cursor

cur.execute('DROP TABLE IF EXISTS Counts')
#this is a gardian line if there is aready a table created it will drop the table

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
#creat the table to hold two viribles

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    org = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))#tuple for email
    #use the cursor to open the file
    row = cur.fetchone()
    #retrieves the next row of a query result set and returns a single sequence !!!
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
                #a gardian for if there is not a row it will creat one
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
        #the ? is a place holder for email
        #uses update because better for multyple connection
    conn.commit()
    #it writes every thing into disc

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
#prints every thing
cur.close()
#closes the curosur
