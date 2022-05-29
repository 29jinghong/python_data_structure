file = input("Enter the file name: ")
fh = open(file)
words = []
words_d = dict()
total = 0
nums= []

for line in fh:
  line = line.strip()
  word = line.split()
  words = words + word

print(words)

for line in words:
  words_d[line] = words_d.get(line, 0) +1

for k,v in words_d.items():
  if (k.strip("\n")).isdigit():
    nums.append(k.strip("\n"))

for num in nums:
  total = total + int(num)

print(total)
