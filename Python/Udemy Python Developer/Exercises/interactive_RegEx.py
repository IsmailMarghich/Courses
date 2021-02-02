#create a password checker with RegEx
#a password that has to be 8 char long
#contain any sort letters, numbers, and $%#@
#it has to also end with a number
import re
password = 'cowmilk$%123' #our password
pattern = re.compile(r"([A-Za-z0-9$%#@]{8,}\d)") #this allow all leters, numbers and the 4 special characters, 
check = pattern.search(password)                 #it also checks wether its longer than 8 characters and ends with a number
print(check)
