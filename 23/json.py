import sqlite3

print("Creating JSON output on food.js...")

conn = sqlite3.connect('foodfacts.sqlite')
cur = conn.cursor()

cur.execute('''SELECT data.foodId, foods.name, data.energy, data.fat, data.carbohydrates, data.fiber, data.proteins, data.salt, foods.url 
    FROM foods JOIN data ON foods.id = data.foodId
    ''')

def check(data):
    if data == "?" :
        return 0
    else:
        return data

fhand = open('food.js','w')

count = 0

#writes in food.js
fhand.write('spiderJson = {"foods":[\n')

for row in cur :
    if count > 0 :
        fhand.write(',\n')
    fhand.write('{' + '"foodId":' + str(row[0]) + ',"name":"' + str(row[1]) + '",')
    fhand.write(' "energy":"' + str(check(row[2])) + '", "fat":"' + str(check(row[3])) + '", "carbohydrates":"' + str(check(row[4])) + '",')
    fhand.write(' "fiber":"' + str(check(row[5])) + '","proteins":"' + str(check(row[6])) + '","salt":"'+str(check(row[7])) + '",')
    fhand.write(' "url":"' + str(check(row[8])) + '"}')
    count = count + 1

fhand.write('\n]\n};')
print('Done!')
cur.close()
