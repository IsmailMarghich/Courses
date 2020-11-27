import PyPDF2 #import pdf to read our pdfs and sys to read inputs from command line
import sys
inputs = sys.argv[1:] #all the files to be merged are all the arguments after the file name

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger() #create a merger object
    for pdf in pdf_list: #for each pdf in the input
        print(pdf)
        merger.append(pdf) #append them to merger
    merger.write('merged.pdf') #write the merged pdfs to a file
pdf_combiner(inputs) #run the function with our inputs