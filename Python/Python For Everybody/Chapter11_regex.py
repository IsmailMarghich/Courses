import re
fname = input("Enter file name: ") #input filename
try: #try opening file
    fh = open(fname)
except: #if file isnt recognized, start over again
    print('File cannot be opened')
    exit()
sum = 0
for line in fh:
    y = re.findall('[0-9]+', line)
    for z in y:
        sum = sum + int(z)
print(sum)