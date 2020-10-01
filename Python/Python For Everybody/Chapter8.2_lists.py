fname = input("Enter file name: ") #input filename
count = 0
try: #try opening file
    fh = open(fname)
except: #if file isnt recognized, start over again
    print('File cannot be opened')
    exit()
for line in fh:
    line = line.rstrip() #strip the lines from white space
    if line == ' ': continue #skips empty lines
    if line.startswith('From'): #picks the lines that start with From
        words = line.split() #split the line into words
        if(len(words)) > 2: #checks the length of the word
            print(words[1]) #prints the second word 
            count = count +1 #add to the counter
print("There were", count, "lines in the file with From as the first word") #print out the result of counter