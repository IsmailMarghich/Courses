import PyPDF2  # import pdf to read our pdfs 

pdf = input('which pdf file do you wanna watermark') #ask for the file name to water mark
input_pdf = PyPDF2.PdfFileReader(open(f'{pdf}', 'rb')) #open the input file in read binary mode
watermark = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb')) #open the watermark file in read binary mode
output = PyPDF2.PdfFileWriter() #make an output object as a file writer

for i in range(input_pdf.getNumPages()): #loop one time for each page in the pdf
    page = input_pdf.getPage(i) #read the file via iterable
    page.mergePage(watermark.getPage(0)) #merge the page with the watermark page
    output.addPage(page) #add page to writer object
    with open('watermarked.pdf', 'wb') as file: #open and create/overwrite a file 
        output.write(file) #write our watermarked page to a file
