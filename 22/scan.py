from contextlib import nullcontext
import urllib.request, urllib.parse, urllib.error
from xml.dom.expatbuilder import FilterVisibilityController
from bs4 import BeautifulSoup
import ssl
import sqlite3
from urllib.request import urlopen

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('foodfacts.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS data''')

cur.execute('''CREATE TABLE IF NOT EXISTS data
    (foodId INTEGER, 
    energy TEXT, 
    fat TEXT,
    carbohydrates TEXT,
    fiber TEXT,
    proteins TEXT,
    salt Text)''')

# cur.execute('select count(*) FROM foods')
# num = cur.fetchone
# print(num())
propertyPrefix = 'food:'
propertySuffix = 'Per100g'
foodData = []

def retrieve(what):
    td = soup.find("td", attrs = {"property" : propertyPrefix + what + propertySuffix})
    if (td != None):
        return td.get('content')
    else:
        return "?"

allRows = cur.execute('SELECT id,url FROM foods')
for row in allRows:
    foodId = int(row[0])
    url = row[1]

    print("-------food id,url-------")
    print("food id: ", foodId)
    print("url: ", url)

    try:
        document = urlopen(url, context=ctx)
        html = document.read()
        soup = BeautifulSoup(html, "html.parser")

    except KeyboardInterrupt:
        print('')
        print('Program interrupted by user...')
        break
    except:
        print("Unable to retrieve or parse page")
        conn.commit()
        continue

    #-----getting energy-----
    print("-----getting energy-----")
    energy = retrieve("energy")
    print(energy)

    #-----getting fat-----
    print("-----getting fat-----")
    fat = retrieve("fat")
    print(fat)

    #-----getting carbohydrates-----
    print("-----getting carbohydrates-----")
    carbohydrates = retrieve("carbohydrates")
    print(carbohydrates)

    #-----getting fiber-----
    print("-----getting fiber-----")
    fiber = retrieve("fiber")
    print(fiber)

    #-----getting proteins-----
    print("-----getting proteins-----")
    proteins = retrieve("proteins")
    print(proteins)

    #-----getting salt-----
    print("-----getting salt-----")
    salt = retrieve("salt")
    print(salt)

    #intserting 
    foodData.append( (foodId, energy, fat, carbohydrates, fiber, proteins, salt) )

#only need to look at this 
#inserting into data table
for facts in foodData:
    print(facts[0])
    print(facts[1])
    print(facts[2])
    print(facts[3])
    print(facts[4])
    print(facts[5])
    print(facts[6])
    cur.execute('INSERT INTO data (foodId, energy, fat, carbohydrates, fiber, proteins, salt) VALUES (?, ?, ?, ?, ?, ?, ?)', (facts[0], facts[1], facts[2], facts[3], facts[4], facts[5], facts[6]))
   
conn.commit()
cur.close()
conn.close()
