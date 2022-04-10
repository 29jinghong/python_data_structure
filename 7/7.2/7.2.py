count   = 0
total   = 0
ipos    = 0
fname   = input("Please type in the file you wanna scan: ")
#tells python what file you wanna open
fhandle = open(fname)

for line in fhandle:
    if line.startswith("X-DSPAM-Confidence"):
        ipos    = line.find(':')
        count   = count+1
        total   = total + float(line[ipos + 1: ])
        #will find the total of all float numbers
if count =! 0:
	print(total/count)
else:
    print("Wrong input!")
#will print out the avrage of "X-DSPAM-Confidence"
