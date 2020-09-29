fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened')
    exit()
count = 0
total = 0.0
for line in fh:
    if line.startswith('X-DSPAM-Confidence: '):
        x = line.find(":")
        y = float(line[x+1:])
        count += 1
        total += y
print('Average spam confidence:', total/count)
print(count)
