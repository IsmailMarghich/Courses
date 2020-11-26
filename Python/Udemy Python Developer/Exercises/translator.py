#build a translator that reads a file and prints a japanese translation of what is in the file
from translate import Translator
translator = Translator(to_lang='ja') #set translation language to japanese
try:
    with open('text.txt', mode='r') as my_file: #open the file as read
       text = my_file.read()
       translation = translator.translate(text) #translate the text with the trnaslate method
       print(translation) #print out our japanese translation
except FileNotFoundError:
    print('file not found')
