fname = input("Enter file name: ") #input filename
try: #try opening file
    fh = open(fname)
except: #if file isnt recognized, start over again
    print('File cannot be opened')
    exit()
count = 0 #declaring starting variables
total = 0.0
for line in fh:
    if line.startswith('X-DSPAM-Confidence: '): #finding lines that start with our target
        x = line.find(":") #find location of :
        y = float(line[x+1:]) #filter out the float from the target
        count += 1 #add to the count
        total += y #add to the total
print('Average spam confidence:', total/count) #print the average confidence
print(count) #print count
