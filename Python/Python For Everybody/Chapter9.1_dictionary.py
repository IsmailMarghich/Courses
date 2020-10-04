counts = dict()

fname = input("Enter file name: ") #input filename
try: #try opening file
    fh = open(fname)
except: #if file isnt recognized, start over again
    print('File cannot be opened')
    exit()
for line in fh:
    line = line.rstrip() #strip the lines from white space
    if not line.startswith("From "): continue
    words = line.split()
    counts[words[1]] = counts.get(words[1],0)+1
maximum = None
maximum_author = None

for key in counts:
    if maximum is None: maximum = counts[key]

    if maximum < counts[key]:
        maximum = counts[key]
        maximum_author = key

print(maximum_author, maximum)