# Python 3 PDF combiner

import os, PyPDF2, sys

# Stores the path to the directory
path = sys.argv[1]

pagesScanned = 0;

# List to store PDF files
pdfFiles = []

# Adds all PDF files to the list
for filename in os.listdir(path):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

# Sorts the PDFs by name
pdfFiles.sort()

pdfWriter = PyPDF2.PdfFileWriter()

# Loops through all the PDF files
for filename in pdfFiles:
    pdfFileObj = open(os.path.join(path,filename), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Loops through all the pages in the PDF and copies them
    for pageNum in range (0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
        pagesScanned = pagesScanned+1
        print(pagesScanned)

# Writes the final PDF file
pdfOutput = open(os.path.join(path,'Merged.pdf'), 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

print("PDFs successfully merged")