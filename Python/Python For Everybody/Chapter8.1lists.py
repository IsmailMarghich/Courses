fname = input("Enter file name: ") #input filename
try: #try opening file
    fh = open(fname)
except: #if file isnt recognized, start over again
    print('File cannot be opened')
    exit()
lst = list()
for line in fh: 
    words = line.split()
    for word in words: #for every word in the file
        if word not in lst: #condition that it isnt already in the list
            lst.append(word) #add the word to the list
print(sorted(lst)) #output the sorted list without duplicated words