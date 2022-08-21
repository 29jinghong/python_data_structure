import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import sqlite3
from urllib.request import urlopen

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('foodfacts.sqlite')
cur = conn.cursor()

conn2 = sqlite3.connect('fooddata.sqlite')
cur2 = conn2.cursor()

cur2.execute('''DROP TABLE IF EXISTS data''')

cur2.execute('''CREATE TABLE IF NOT EXISTS data
    (id INTEGER PRIMARY KEY, 
    energy TEXT, 
    fat TEXT,
    carbohydrates TEXT,
    fiber TEXT,
    proteins TEXT,
    salt Text)''')

#cur.execute('SELECT COUNT(*) FROM foods')
#num = cur.fetchone
num = 1
while True:
    cur.execute('SELECT id,name,url FROM foods WHERE id=?', (num,))
    try:
        row = cur.fetchone()
        id = row[0]
        name = row[1]
        url = row[2]
    except:
        print('the end')
        many = 0
        break
    print("-------id,name,url-------")
    print(id," ", name, " ", url)
    num = num + 1

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

    tags = soup('a')

    #-----getting energy-----
    try:
        
        energyt = soup.find("td", attrs = {"property" : "food:energyPer100g"})
        #print("-----energyt-----")
        #print(energyt)
        energy = energyt.get("content")
        print("-----energy-----")
        print(energy)
        print("-----energy-----")
        print("cant find energy")
        energy = "?"
    except:
        print("-----energy-----")
        print("cant find energy")
        energy = "?"
        
    #-----getting fat-----
    try:
        fatt = soup.find("td", attrs = {"property" : "food:fatPer100g"})
        #print("-----fatt-----")
        #print(fatt)
        fat = fatt.get("content")
        print("-----fat-----")
        print(fat)
    except:
        print("-----fat-----")
        print("cant find fat")
        fat = "?"

    #-----getting carbohydrates-----
    try:
        carbohydratest = soup.find("td", attrs = {"property" : "food:carbohydratesPer100g"})
        #print("-----carbohydratest-----")
        #print(carbohydratest)
        carbohydrates = carbohydratest.get("content")
        print("-----carbohydrates-----")
        print(carbohydrates)
    except:
        print("-----carbohydrates-----")
        print("cant find carbohydrates")
        carbohydrates = "?" 

    #-----getting fiber-----
    try:
        fibert = soup.find("td", attrs = {"property" : "food:fiberPer100g"})
        #print("-----fibert-----")
        #print(fibert)
        fiber = fibert.get("content")
        print("-----fiber-----")
        print(fiber)
    except:
        print("-----fiber-----")
        print("cant find fiber")
        fiber = "?"

    #-----getting proteins-----
    try:
        proteinst = soup.find("td", attrs = {"property" : "food:proteinsPer100g"})
        #print("-----proteinst-----")
        #print(proteinst)
        proteins = proteinst.get("content")
        print("-----proteins-----")
        print(proteins)
    except:
        print("-----proteins-----")
        print("cant find proteins")
        proteins = "?"

    #-----getting salt-----
    try:
        saltt = soup.find("td", attrs = {"property" : "food:saltPer100g"})
        #print("-----saltt-----")
        #print(saltt)
        salt = saltt.get("content")
        print("-----salt-----")
        print(salt)
    except:
        print("-----salt-----")
        print("cant find salt")
        salt = "?"
    
    cur2.execute('INSERT INTO data (energy, fat, carbohydrates, fiber, proteins, salt) VALUES (?, ?, ?, ?, ?, ?)', (energy, fat, carbohydrates, fiber, proteins, salt))
    conn2.commit()

conn2.commit()
conn.commit()
cur.close()
conn.close()
cur2.close()
conn2.close()