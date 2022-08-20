posx = 0
posy = 0
f = open("data.txt", "r")
for i in f:
    line = i
    if(line.find('<span>')!= -1):
        posx = line.find('-&nbsp;')
        posy = line.find('"', posx)
        print(i[posx+7:posy])