import sqlite3

print("Creating JSON output on food.js...")

conn = sqlite3.connect('foodfacts.sqlite')
cur = conn.cursor()

cur.execute('''SELECT COUNT(id) AS  foodId,name, energy, fat, carbohydrates, fiber, proteins, salt, url 
    FROM foods JOIN data ON foods.id = data.foodId
    GROUP BY id ORDER BY foodId''')

fhand = open('food.js','w')

nodes = list()
foodDatas = []
count = 0

for row in cur :
    nodes.append(row)
    foodId = row[0]
    foodName = row[1]
    energy = row[2]
    fat = row[3]
    carbohydrates = row [4]
    fiber = row[5]
    proteins = row[6]
    salt = row[7]
    url = row[8]
    foodDatas.append( (foodId, foodName, energy, fat, carbohydrates, fiber, proteins, salt, url) )

#writes in food.js
fhand.write('spiderJson = {"foods":[\n')

for row in foodDatas:
    if count > 0 :
        fhand.write(',\n')
    fhand.write('{'+'"foodId":'+str(row[0])+',"name":'+str(row[1])+',')
    fhand.write(' "energy":'+str(row[2])+', "fat":"'+str(row[3])+', "carbohydrates":"'+str(row[4])+',')
    fhand.write(' "fiber":'+str(row[5])+',"proteins":'+str(row[6])+',"salt":'+str(row[7])+',')
    fhand.write(' "url":'+str(row[8])+'"}')
    count = count + 1

fhand.write(']};')
print('Done!')
cur.close()