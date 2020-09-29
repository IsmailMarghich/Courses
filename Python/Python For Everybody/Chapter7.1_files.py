#filename
fname = input('Enter the file name: ')

#asks for file name and if its invalid, let the user know
try:
	fhand = open(fname)
except:
	print("File cannot be opened: ", fname)
	exit()
#loops through file and makes it uppercase
for line in fhand:
    linestripped = line.rstrip()
    print(linestripped.upper())