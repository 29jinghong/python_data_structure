import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
#connects with geodata.sqlite

cur = conn.cursor()
#creats a cursor that could be used works like the file handle

cur.execute('SELECT * FROM Locations')
#https://www.w3resource.com/sqlite/sqlite-select-query-statement.php
#will select all the data from location

fhand = codecs.open('where.js', 'w', "utf-8")
#open the file where.js using the given mode and return an instance of StreamReaderWriter
#https://docs.python.org/3/library/codecs.html
#Creates a StreamReaderWriter instance. stream must be a file-like object. Reader and Writer must be factory functions or classes providing the StreamReader and StreamWriter interface resp. Error handling is done in the same way as defined for the stream readers and writers.

fhand.write("myData = [\n")
#https://www.geeksforgeeks.org/file-handling-python/
#it allows us to write in the file

count = 0
#sets a count of how many data is wroten in where.js

for row in cur :
    data = str(row[1].decode())
    #for every row it will decode it and set the data to the string

    try:
        js = json.loads(str(data))
    #tryes to load the joson so it doest blow up
    except:
        continue
    #if the try blows up it will continew

    if not('status' in js and js['status'] == 'OK') :
        continue
    #dont know what this line does^

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    #gets the lat and the lng by going throw js^

    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    #gets the formatted address from js^

    where = where.replace("'", "")
    #replace() is an inbuilt function in the Python programming language that returns a copy of the string where all occurrences of a substring are replaced with another substring. 
    #https://www.geeksforgeeks.org/python-string-replace/#:~:text=replace()%20is%20an%20inbuilt,are%20replaced%20with%20another%20substring.&text=Parameters%20%3A,substring%20you%20want%20to%20replace.
    try :
        print(where, lat, lng)

        count = count + 1
        #addes one count to count

        if count > 1 : fhand.write(",\n")
        #if there is more than one line it will add a \n to make a new line so it doest blow up
        #also thats how the json format works.

        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        #saves outputs as the lat, lng, and where

        fhand.write(output)
        #saves output into the where.js, in a json format
    except:
        continue
    #if where or lat or lng doesent work or if the .write function donesent work it will continue in the back

fhand.write("\n];\n")
#ends the json format

cur.close()
#ends the cursor

fhand.close()
#closes the file handle

print(count, "records written to where.js")
print("Open where.html to view the data in a browser")
#prints where the data is stored(where.html), and howmuch data is in it.

