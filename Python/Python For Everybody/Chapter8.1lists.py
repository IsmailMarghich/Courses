fname = input("Enter file name: ") #input filename
try: #try opening file
    fh = open(fname)
except: #if file isnt recognized, start over again
    print('File cannot be opened')
    exit()
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
print(sorted(lst))