
xfile = open('mbox-short.txt')
#how to acces other files thats not under this filder?
#example if you wanna acces mbox you can just "xfile = open('mbox-short.txt')"
#but if you wanna acces for example a file under test how do you acces it?
for line in xfile:
    line = line.rstrip()
    #this is used to remove the extra space on the line.
    print(line.upper())

#I name this handle is because open returns a handdle of the file
fhandle = open('mbox-short.txt')
#named this text because its the text sored in mbox-short
text =''
for line in fhandle
    text = text + line.upper()
print(text)
