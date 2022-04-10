#takes the file and make a handle for it.
name = input("Enter file name: ")
if len(name)<1:
  name = 'mbox-short.txt'
handle = open(name)

#takes out the time.
time_d = dict()
time  = []
for line in handle:
  if line.startswith("From "):
    words = line.split()
    hour = words[5].split(':')
    time_d[hour[0]] = time_d.get(hour[0], 0) + 1

#The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
#put the value in to a pare and sort it.
for k,v in time_d.items():
  time.append((k,v))

time.sort()

for k,v in time:
  print(k,v)
