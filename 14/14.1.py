import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

data = ''
total = 0
link = 'http://py4e-data.dr-chuck.net/comments_42.xml'

fhand = urllib.request.urlopen(link)
for line in fhand:
  word = line.decode()
  data = (data + word)

tree = ET.fromstring(data)
nums = tree.findall('.//count')

for num in nums:
  number = num.text
  total = total + int(number)
print("total :", total)
