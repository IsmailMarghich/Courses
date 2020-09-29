fname = input("Enter file name: ") #input filename
count = 0
try: #try opening file
    fh = open(fname)
except: #if file isnt recognized, start over again
    print('File cannot be opened')
    exit()
for line in fh:
    line = line.rstrip()
    if line == ' ': continue
    if line.startswith('From'):
        words = line.split()
        if(len(words)) > 2:
            print(words[1])
            count = count +1
print("There were", count, "lines in the file with From as the first word")