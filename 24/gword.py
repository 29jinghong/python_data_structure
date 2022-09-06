import sqlite3
import time
import zlib
import string

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

#reades all the subject from subjects data table, and store it in subjects.
cur.execute('SELECT id, subject FROM Subjects')
subjects = dict()
for message_row in cur :
    subjects[message_row[0]] = message_row[1]

# cur.execute('SELECT id, guid,sender_id,subject_id,headers,body FROM Messages')
cur.execute('SELECT subject_id FROM Messages')
counts = dict()
for message_row in cur :
    #strips and convert to lower which keeps tomany words from showing up
    text = subjects[message_row[0]]
    #str.maketrans throws away puntuations and numbers wich when you are reading you dont get dashes and stuff.
    text = text.translate(str.maketrans('','',string.punctuation))
    text = text.translate(str.maketrans('','','1234567890'))
    text = text.strip()
    text = text.lower()
    words = text.split()
    #counts each word in words.
    for word in words:
        if len(word) < 4 : continue
        counts[word] = counts.get(word,0) + 1
    #basicaly a only word count.

x = sorted(counts, key=counts.get, reverse=True)
#sorts the words

highest = None
lowest = None
for k in x[:100]:
    #this figures out what the highes and lowest count word is.
    if highest is None or highest < counts[k] :
        highest = counts[k]
    if lowest is None or lowest > counts[k] :
        lowest = counts[k]
print('Range of counts:',highest,lowest)

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

#writes the java script data into gword.js file.
fhand = open('gword.js','w')
fhand.write("gword = [")
first = True
for k in x[:100]:
    if not first : fhand.write( ",\n")
    first = False
    #text normalisation(how big each word is)
    size = counts[k]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '"+k+"', size: "+str(size)+"}")
fhand.write( "\n];\n")
fhand.close()

print("Output written to gword.js")
print("Open gword.htm in a browser to see the vizualization")
