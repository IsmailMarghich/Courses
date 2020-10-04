fname = input("Enter file name: ") #input filename
try: #try opening file
    fh = open(fname)
except: #if file isnt recognized, start over again
    print('File cannot be opened')
    exit()
hcount = dict() #declare our starting variables
hlst = []
for line in fh: 
    words = line.split() #split every line up
    if len(words) > 2 and words[0] == 'From':       #select the lines we need
        hr = words[5].split(':')                    #grab the 5th part of the splitted line(the time section) and split this with ':'
        hcount[hr[0]] = hcount.get(hr[0], 0) + 1    #count the amount of each hour in a dictionary
    else:
        continue

for k,v in hcount.items():                           #k = hour v = count
    hlst.append((k,v))                               #append the k,v tuple to the list

hlst.sort()                                         #sort the list (we cant sort a tuple so we use the list to sort the k)
for k,v in hlst:                                    #for every k,v pair print the hour and the amount of times it appared
    print (k,v)         