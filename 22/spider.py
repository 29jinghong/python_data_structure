import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import sqlite3

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('foodfacts.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS foods''')

cur.execute('''CREATE TABLE IF NOT EXISTS foods
    (id INTEGER PRIMARY KEY, 
    name TEXT, 
    url TEXT UNIQUE)''')


url = 'https://world.openfoodfacts.org'
response = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(response, "html.parser")

resultDiv = soup.find("div", attrs = {"id" : "search_results"})
allLis = resultDiv.find_all("li")
#print(allLis)

for li in allLis:
    aTag = li.find("a")   #same as li.find("a")
    foodUrl = url + aTag.get("href", None)
    print(foodUrl)

    span = aTag.find("span")
    print(span.text)
    print()
    cur.execute('INSERT INTO foods (name, url) VALUES (?, ?)', (span.text,foodUrl))

conn.commit()
cur.close()
conn.close()