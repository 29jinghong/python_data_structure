fh = open('romeo.txt')
wordsS = []
#search
for line in fh:
  word = line.split()
  if word not in wordsS:
    wordsS.append(word)
print(sorted(wordsS))
