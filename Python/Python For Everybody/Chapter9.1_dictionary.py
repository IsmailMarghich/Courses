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
    counts[words[1]] = counts.get(words[1],0)+1 #grabs the email from the line, and gets it count
maximum = None #declare variables 
maximum_author = None

for key in counts: #for each key
    if maximum is None: maximum = counts[key] #if its none, start off by adding the first key

    if maximum < counts[key]: #if the value of the current key is smaller than the new key
        maximum = counts[key] #add the new maximum 
        maximum_author = key #add the key to the author of the largest value

print(maximum_author, maximum) #print the most common name and its value