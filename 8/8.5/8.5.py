#fname = input("Enter file name: ")
#if (len(fname)<1):
fname = "mbox-short.txt"

fh    = open(fname)
count = 0
data  = []
for line in fh:
  if (line.startswith("From ")):
    #this finds the line that start with 'from'
    frag = line.split()
    #makes the line into a list by each word
    data.append(frag[1])
    #finds the email adress and put in the data

for line in data:
    print(line)
print("There were", len(data), "lines in the file with From as the first word")
